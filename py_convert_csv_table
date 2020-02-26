#                                   Convert CSV Table
#                   From This         -->                 To This
#   +-----------+--------+-------+---------+    +-----------+---------+
#   | Reference | Apples | Pears | Bananas |    | Reference | Desc    |
#   +-----------+--------+-------+---------+    +-----------+---------+
#   | 1         | X      | X     |         |    | 1         | Apples  |
#   +-----------+--------+-------+---------+    +-----------+---------+
#   | 2         |        | X     | X       |    | 1         | Pears   |
#   +-----------+--------+-------+---------+    +-----------+---------+
#   | 3         |        |       | X       |    | 2         | Pears   |
#   +-----------+--------+-------+---------+    +-----------+---------+
#                                               | 2         | Bananas |
#                                               +-----------+---------+
#                                               | 3         | Bananas |
#                                               +-----------+---------+

import pandas as pd
df=pd.read_csv(r'Path_to_csv')
# df=df[:-n] if csv has n trailing empty rows, exclude them 
   
fn="filename" # define file name for export
edf= pd.DataFrame(columns=['Ref','Desc'])                                                                   #create empty dataframe with two columns 

i=0
j=0
while i < df.shape[0]:                                                                                      #   i loops through number of rows in the dataframe (i.e. .shape[0])
    while j < df.shape[1]:                                                                                  #   j loops through number of columns in the dataframe (i.e. .shape[1])
        #print(str(i)+str(j))
        if df.iloc[i,j] == "X":                                                                             #   if location i,j meets condition "X" then 
            edf=edf.append({'Ref':(df['Col1'])[i],'Desc':(df.columns.values)[j]},ignore_index=True)         #       append to edf: value in i'th row  from column named Col1 under 'Ref'; title of j'th column under 'Desc'
        j=j+1    
    j=0                                                                                                     
    i=i+1


print(edf)
edf.to_csv(r'Path_to_folder'+fn+'.csv',index=False)                                                         #    export to csv
