import pandas as pd 
import numpy as np

df1=pd.DataFrame({'A':[1,np.nan,3],'B':[4,5,np.nan]})
print("\nOriginal DataFrame with missing data:")
print(df1)

print("\nFill missing values with 0:")
print(df1.fillna(0))

print("\nDrop rows with missing data")
print(df1.dropna())

print("\nCheck where data is missing")
print(df1.isnull())