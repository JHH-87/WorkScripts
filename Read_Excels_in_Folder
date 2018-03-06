
import os
import pandas as pd
import xlrd

# Enter directory with files
PATH = r"\\directory"

# obtain only files with permission to read
cwd = os.getcwd()
os.chdir(PATH)
wbs = [f for f in os.listdir(PATH) if os.path.isfile(f)]
wbs = [f for f in wbs if '~' not in f and 'xlsx' in f]

# get number of workbooks 
n_wbs = len(wbs)
print(n_wbs)

# define empty variables
ao = ""
sa_ac = 0
pa_ac = 0
sa_bu = 0
pa_bu = 0
i=-1    

#define dataframe 
df=pd.DataFrame.from_records({'index':[i],'AreaOffice':[ao],'SalesActual':[sa_ac],'PayrollActual':[pa_ac],'SalesBudget':[sa_bu],'PayrollBudget':[pa_bu]})

#iterate through workbooks

for i in range(0,n_wbs):
    wb = xlrd.open_workbook(os.listdir('.')[i])
    
    
    worksheet = wb.sheet_by_index(1)

# cell reference is (row,column)
    ao = worksheet.cell(3,2).value
    sa_ac = worksheet.cell(10,2).value
    pa_ac = worksheet.cell(33,2).value
    sa_bu = worksheet.cell(10,3).value
    pa_bu = worksheet.cell(33,3).value
    
    df2=pd.DataFrame.from_records({'index':[i],'AreaOffice':[ao],'SalesActual':[sa_ac],'PayrollActual':[pa_ac],'SalesBudget':[sa_bu],'PayrollBudget':[pa_bu]})
    
    df=pd.concat([df,df2])
    
    print(str(i)+ao)

    i=i+1

df
df.to_csv(PATH+"/CONSOL.csv")
