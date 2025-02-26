"""
## 데이터분석용 패키지 (pandas, numpy, scipy, seaborn, datetime, sklearn)
"""

import numpy as np
import pandas as pd

"""
## pandas DataFrame 다루기
"""

resource_dir = "C:/Users/ilma0/PycharmProjects/cptpyworkshop/resource_for_workshop"
input_dir = f"{resource_dir}/SAS_RawData(csv)"
output_dir = f"{resource_dir}/prep_data"

## Data Load

scn_to_sjn_rdf = pd.read_excel(f"{resource_dir}/A101_06FDI2404_Disposition.xlsx")
adm_rdf = pd.read_csv(f"{input_dir}/ex.csv")
conc_time_rdf = pd.read_csv(f"{input_dir}/pc.csv")

df = pd.read_csv(f"{output_dir}/CKD383_ConcPrep_Metformin(Phoenix).csv")

## DataFrame의 구조
# index, row, column,

list(df.index)
list(df.columns)
pd.Series

pd.DataFrame({'ID':[1,2,3,4,5,6,7], 'SEX':['F','M','F','M','F','M','M']})

## 로드, 슬라이싱, index 와 columns 조작

# index, columns: 특정 컬럼 조회 / 특정 컬럼들이 포함된 DataFrame 조회 / 특정 컬럼 추가

df['ID']
df['CONC']
df[['ID','ATIME','CONC']]

df['Project'] = 'CKD-383'

df['SEQUENCE'] = 1
df['SEQUENCE'] = df['ID']
df['SEQUENCE'] = df['ID'].map(lambda x:x[0])
df['SEQUENCE'] = df['SEQUENCE'].map({'A':1,'B':2})

seq_dict = {'A':1,'B':2}
df['SEQUENCE'] = df['ID'].map(lambda x:seq_dict[x[0]])


df = df.rename(columns={'DRUG':'ADM_DRUG','FEEDING':'FED'})
df = df.rename(columns={'ADM_DRUG':'DRUG','FED':'FEEDING'})

# 슬라이싱: loc[], iloc[], at[], iat[]

df.iloc[4,4]

df.iloc[4:10, 4:9]
df.iloc[4:300:2, 4:9:2]
df.loc[4:10, 'ATIME']
df.loc[4:10, 'ATIME':]

df.iat[2,7]
df.at[1,'CONC']


# 조건에 맞는 row 선택

df['CONC']=='.'
df[df['CONC']=='.']
df[df['CONC'] > '50']
df[df['CONC'] <= '0.0']
df[(df['FEEDING']=='FED')&(df['CONC'] == '.')]
df[(df['ATIME']<2)|(df['CONC'] == '.')]

# replace, astype, isna

df['CONC2'] = df['CONC'].replace('.',np.nan)
df['CONC2'] = df['CONC2'].astype(float)
df['CONC2'] = df['CONC'].replace('.',np.nan).astype(float)

df[~df['CONC2'].isna()]

# 결측치 처리(dropna(axis=1), fillna('.'), fillna(method='ffill')

df.dropna(axis=0)    # NA 존재하는 행 삭제
df.dropna(axis=1)    # NA 존재하는 열 삭제
df.fillna('.')
df.fillna(method='ffill')
df.fillna(method='bfill')

# sort_values, reset_index, set_index

ndf = df.sort_values(['CONC2','PERIOD'])
ndf = ndf.reset_index(drop=True)
ndf.set_index(keys=['ID','PERIOD'])


df['AGE'].unique()
for k, fdf in df.groupby(['AGE']):
    break

df.groupby(['AGE']).agg({'PID':'count', 'AMT':'first', 'TIME':'last'})


for pid in df['PID'].unique():
    frag_df = df[df['PID']==pid]
    frag_df['']
    # if

# 컬럼끼리 연산
# 컬럼값을 연산 ds.mean(), .min(), .max(), .sum(), .median(), .quantile(0.3), .count(), first(), .last()




# df.merge(df2, how='left', on=['id','TAD'])
# pd.concat([df1, df2], axis=0)

# df.groupby(['Formulation','Dose']).agg({'id':'count', 'Dose':'mean', 'TAD':'last'})

# df['id'].map(lambda x:x.split('_'))
# apply, applymap

# df.melt(id_vars=['province'], var_name='sex', value_name='average_float_age')

# for inx, row in df.iterrows():
#      ~~

"""
## Project 실전 연습
"""
