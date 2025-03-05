import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# result_type = 'Phoenix'
result_type = 'R'

resource_dir = "C:/Users/ilma0/PycharmProjects/cptpyworkshop/resource_for_workshop"
input_dir = f"{resource_dir}/SAS_RawData(csv)"
output_dir = f"{resource_dir}/prep_data"

conc_value_rdf = pd.read_csv(f"{resource_dir}/Conc_RawData/CKD-383 FDI CONC - Metformin_Conc.csv")
scn_to_sjn_rdf = pd.read_excel(f"{resource_dir}/A101_06FDI2404_Disposition.xlsx")
adm_rdf = pd.read_csv(f"{input_dir}/ex.csv")
conc_time_rdf = pd.read_csv(f"{input_dir}/pc.csv")


"""
['ID', 'DOSE', 'NTIME', 'ATIME', 'CONC', 'PERIOD', 'FEEDING', 'DRUG']
"""

# Screening number <-> ID   변환시키는 dictionary 만들어두기

scn_to_sjn_rdf['ID'] = scn_to_sjn_rdf['SubjectNr']
scn_to_sjn_rdf['SID'] = scn_to_sjn_rdf['ScreeningNr']
scn_to_sjn_rdf = scn_to_sjn_rdf.dropna(axis=0).reset_index(drop=True)
sid_to_id_dict = dict()
id_to_dict = dict()
for inx, row in scn_to_sjn_rdf[['ID','SID']].iterrows():
    sid_to_id_dict.update({row['SID']:row['ID']})
    id_to_dict.update({row['ID']:row['SID']})

pk_analysis_set_list = scn_to_sjn_rdf[scn_to_sjn_rdf['Pharmacokinetic Set']=='O']['ID']

conc_value_rdf = pd.melt(conc_value_rdf, id_vars=['Drug', 'Period', 'Subjects'], var_name='NTIME', value_name='CONC')

conc_value_rdf['DRUG'] = 'Metformin'
conc_value_rdf['ID'] = conc_value_rdf['Subjects']
conc_value_rdf['SID'] = conc_value_rdf['ID'].map(id_to_dict)
conc_value_rdf['PERIOD'] = conc_value_rdf['Period']
conc_value_rdf = conc_value_rdf[['DRUG','ID','SID','PERIOD','NTIME','CONC']]

adm_rdf['SID'] = adm_rdf['Subject']
adm_rdf['ID'] = adm_rdf['SID'].map(sid_to_id_dict)
adm_rdf['PERIOD'] = adm_rdf['Folder'].map(lambda x:int(x[1:2]))
adm_rdf['ADM_TIME_DT'] = adm_rdf['EXSTDAT_C']
adm_rdf['FEEDING'] = adm_rdf['EXTRT_STD']
adm_rdf = adm_rdf[['ID', 'SID', 'PERIOD', 'ADM_TIME_DT', 'FEEDING']]

conc_time_rdf['SID'] = conc_time_rdf['Subject']
conc_time_rdf['ID'] = conc_time_rdf['SID'].map(sid_to_id_dict)
conc_time_rdf['PERIOD'] = conc_time_rdf['Folder'].map(lambda x:int(x[1:2]))
conc_time_rdf['NTIME'] = conc_time_rdf['PCTPT'].map(lambda x:x.split(' ')[0])
conc_time_rdf['ATIME_DT'] = conc_time_rdf['PCDAT_C']
conc_time_rdf = conc_time_rdf[['ID', 'SID', 'PERIOD', 'NTIME', 'ATIME_DT']]

prep_df = conc_value_rdf.merge(adm_rdf, how='left',on=['ID', 'SID', 'PERIOD'])
prep_df = prep_df.merge(conc_time_rdf, how='left',on=['ID', 'SID', 'PERIOD', 'NTIME'])
prep_df['DOSE'] = 2000

(datetime.strptime('2024-07-23 09:00:00','%Y-%m-%d %H:%M:%S') - datetime.strptime('2024-07-23 08:48:00','%Y-%m-%d %H:%M:%S')).total_seconds()/3600

prep_df['NTIME'] = prep_df['NTIME'].map(lambda x:float(x.replace('h','')))

# row = {'ATIME_DT':'2024-08-01 09:10:00', 'ADM_TIME_DT':'2024-07-30 09:54:00'}
prep_df['ATIME'] = prep_df.apply(lambda row: (datetime.strptime(row['ATIME_DT'],'%Y-%m-%d %H:%M:%S')-datetime.strptime(row['ADM_TIME_DT'],'%Y-%m-%d %H:%M:%S')).total_seconds()/3600 if isinstance(row['ATIME_DT'],str) and isinstance(row['ADM_TIME_DT'],str) else np.nan, axis=1)
prep_df['ATIME'] = prep_df['ATIME'].clip(lower=0)

# 채혈 되지 않은 대상자 분석에서 제외
prep_df = prep_df[prep_df['CONC']!='-'].sort_values(['DRUG','ID','PERIOD','ATIME'],ignore_index=True)

first_float_index_dict = dict()
for inx, frag_df in prep_df.groupby(['DRUG','ID','PERIOD']):
    # if inx[0]=='Lobeglitazone': raise ValueError
    frag_df['CONC']
    first_index = frag_df.index[0]
    first_float_index = -1
    for finx, row in frag_df.iterrows():
        try:
            float(row['CONC'])
            first_float_index = finx
            break
        except:
            continue

    first_float_index_dict.update({f"{inx[0]}_{inx[1]}_{inx[2]}" : (first_index ,first_float_index)})

for inx, row in prep_df.iterrows():
    key = f"{row['DRUG']}_{row['ID']}_{row['PERIOD']}"

    if (first_float_index_dict[key][0]<=inx) and (first_float_index_dict[key][1] > inx) and (row['CONC'] == 'BLQ'):
        prep_df.at[inx,'CONC'] = 0.0
    elif (row['NTIME'] != 0) and (row['CONC'] == 'BLQ'):
        prep_df.at[inx, 'CONC'] = np.nan
    elif (row['NTIME'] != 0) and (row['CONC'] != 'BLQ'):
        prep_df.at[inx, 'CONC'] = float(prep_df.at[inx, 'CONC'])
    else:
        raise ValueError

# raise ValueError
if result_type == 'Phoenix':
    prep_df['CONC'] = prep_df['CONC'].map(lambda x: str(x) if not np.isnan(x) else '.')
    prep_df = prep_df[['ID', 'DOSE', 'NTIME', 'ATIME', 'CONC', 'PERIOD', 'FEEDING', 'DRUG']]

    unit_row_dict = {'DOSE': 'mg', 'NTIME': 'h', 'ATIME': 'h', 'CONC': 'ng/mL'}
    additional_row = dict()
    for c in list(prep_df.columns):
        try:
            additional_row[c] = unit_row_dict[c]
        except:
            additional_row[c] = ''
    prep_df = pd.concat([pd.DataFrame([additional_row], index=['', ]), prep_df])
elif result_type == 'R':
    prep_df = prep_df.dropna()

prep_df = prep_df[['ID', 'DOSE', 'NTIME', 'ATIME', 'CONC', 'PERIOD', 'FEEDING', 'DRUG']].sort_values(['DRUG','ID','PERIOD','NTIME'])

result_file_name = f"CKD383_ConcPrep_({result_type}).csv"
result_file_path = f"{output_dir}/{result_file_name}"
prep_df.to_csv(result_file_path, header=True, index=False)

# 약물별로 나눠서도 저장
for drug in drug_dose_dict.keys():
    result_file_name = f"CKD383_ConcPrep_{drug}({result_type}).csv"
    result_file_path = f"{output_dir}/{result_file_name}"
    prep_df[prep_df['DRUG']==drug].to_csv(result_file_path, header=True, index=False)


# prep_df['ADM_TIME_DT']
# timedelta()
# for inx, row in prep_df.iterrows():
# 'ID', 'DOSE', 'NTIME', 'ATIME', 'CONC', 'PERIOD', 'FEEDING', 'DRUG'
# conc_value_rdf.columns


# Subject / Period /