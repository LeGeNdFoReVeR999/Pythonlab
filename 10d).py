import pandas as pd 
import numpy as np

left=pd.DataFrame({'Key':['A','B','C'],'val1':[1,2,3]})
right=pd.DataFrame({'Key':['B','C','D'],'val2':[4,5,6]})

merged=pd.merge(left,right,on='Key',how='outer')
print("\nMerged dataframe(outerjoin):")
print(merged)

df=pd.DataFrame({
    'Department':['HR','HR','IT','IT'],
    'Salary':[3000,4000,5000,6000]
})
print("\nGroup by department and sum salaries:")
print(df.groupby('Department').sum())
