import numpy as np
import pandas as pd

## Data Load

df = pd.read_csv('C:/Users/ilma0/PycharmProjects/cptpyworkshop/resource_for_workshop/VO6_5.csv')
mdf = pd.read_csv('C:/Users/ilma0/PycharmProjects/cptpyworkshop/resource_for_workshop/missingdata.csv')

mdf.iloc[:,:-2]
df
df.columns
mdf.columns
mdf = mdf.rename(columns={'Unnamed: 0':'ID','TAD1':'TIME','dose2':'AMT'})
mdf = mdf.iloc[:,:-2]
mdf['DV']='.'
mdf['MDV']=1
mdf['CMT']=1
mdf['RATE'] = mdf['AMT']
demo_df = df[df['ID'].isin(mdf['ID'].unique())].loc[:,['ID']+list(df.columns[7:])].drop_duplicates(['ID'])
modi_mdf = mdf.merge(demo_df, on=['ID'], how='left')[df.columns]

result_df = pd.concat([df,modi_mdf]).sort_values(['ID','TIME','DV'], ascending=[True,True,False])
result_df.to_csv('C:/Users/ilma0/PycharmProjects/cptpyworkshop/resource_for_workshop/result_df.csv')
