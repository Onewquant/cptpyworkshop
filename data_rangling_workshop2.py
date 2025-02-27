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


met_conc_rdf = pd.read_csv(f"{resource_dir}/Conc_RawData/CKD-383 FDI CONC - Metformin_Conc.csv")
scn_to_sjn_rdf = pd.read_excel(f"{resource_dir}/A101_06FDI2404_Disposition.xlsx")
adm_rdf = pd.read_csv(f"{input_dir}/ex.csv")
conc_time_rdf = pd.read_csv(f"{input_dir}/pc.csv")

df = pd.read_csv(f"{output_dir}/CKD383_ConcPrep_Metformin(Phoenix).csv")

## DataFrame의 구조
# index, row, column,

list(df.index)
list(df.columns)
pd.Series([1,2,3,4,5,6,7])

pd.DataFrame({'ID':[1,2,3,4,5,6,7], 'SEX':['F','M','F','M','F','M','M']})

## 로드, 슬라이싱, index 와 columns 조작

# index, columns: 특정 컬럼 조회 / 특정 컬럼들이 포함된 DataFrame 조회 / 특정 컬럼 추가

df['ID']
df['CONC']
df[['ID','ATIME','CONC']]

df['Project'] = 'CKD-383'

df['SEQUENCE'] = 1
df['SEQUENCE'] = df['ID']

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

# unique

ndf['ID'].unique()
ndf['NTIME'].unique()

# 컬럼끼리 연산

ndf['CONC2'] + ndf['CONC2']
ndf['CONC2'] - ndf['CONC2']
ndf['CONC2'] * ndf['CONC2']
ndf['CONC2'] / ndf['CONC2']

# 컬럼값을 연산 .min(), ds.mean(), .max(), .sum(), .median(), .quantile(0.3), .count(), first(), .last()

ndf['CONC2'].first()
ndf['CONC2'].min()
ndf['CONC2'].mean()
ndf['CONC2'].max()
ndf['CONC2'].sum()
ndf['CONC2'].median()
ndf['CONC2'].quantile(0.3)
ndf['CONC2'].last()

# clip()

ndf['CONC2'].clip(3,20)

# map, apply, applymap, iterrows()

df['SEQUENCE'] = df['ID'].map(lambda x:x[0])
df['SEQUENCE'] = df['SEQUENCE'].map({'A':1,'B':2})

seq_dict = {'A':1,'B':2}
df['SEQUENCE'] = df['ID'].map(lambda x:seq_dict[x[0]])

# groupby

for k, fdf in ndf.groupby(['ID']):
    print(fdf)
    break

ndf.groupby(['ID']).agg({'ID':'count', 'CONC2':'max', 'ATIME':'last'})

ndf.groupby(['ID','PERIOD']).agg({'ID':'count', 'CONC2':'max', 'ATIME':'last'})

# merge

ndf['TEST_COL1']=list(range(len(df)))
ndf['TEST_COL2']=list(np.ones(len(df)))
df.merge(ndf[['ID', 'ATIME', 'TEST_COL1', 'TEST_COL2']], how='left', on=['ID','ATIME'])

# concat

df1 = ndf.iloc[:10]
df2 = ndf.iloc[30:50]
pd.concat([df1, df2], axis=0)

# melt

met_conc_rdf.melt(id_vars=['Drug','Period','Subjects'], var_name='NTIME', value_name='CONC')

"""
## Project 실전 연습
"""
