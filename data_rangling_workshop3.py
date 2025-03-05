from pynca.tools import *

resource_dir = 'C:/Users/ilma0/PycharmProjects/testpynca/practice/CKD383FDI/resources'
df = pd.read_csv(f'{resource_dir}/prep_data/CKD383_ConcPrep_(R).csv')

result = tblNCA(df, key=["DRUG", "ID", "FEEDING"], colTime="ATIME", colConc="CONC",
                dose='DOSE', adm="Extravascular", dur=0, doseUnit="mg",
                timeUnit="h", concUnit="ug/L", down="Log", R2ADJ=0,
                MW=0, SS=False, iAUC="", excludeDelta=1, slopeMode='SNUHCPT', colStyle='pw')

result.to_excel(f'{resource_dir}/prep_data/Final Parameters Pivoted.xlsx', index=False, encoding='utf-8')

