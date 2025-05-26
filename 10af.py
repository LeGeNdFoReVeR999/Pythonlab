import pandas as pd 
import numpy as np

# Single level indexing
data = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print("Single level indexing Series:")
print(data)

# Multi-level (hierarchical) indexing
multi_index = pd.MultiIndex.from_tuples([('A', 1), ('A', 2), ('B', 1)])
multi_series = pd.Series([100, 200, 300], index=multi_index)
print("\nHierarchical Series:")
print(multi_series)

# Accessing data
print("\nAccessing multi-level data:")
print("multi_series['A', 1]:", multi_series['A', 1])
print("\nmulti_series['A']:\n", multi_series['A'])
print("\nmulti_series.loc['A', 2]:", multi_series.loc['A', 2])
print("\nmulti_series.loc['B']:\n", multi_series.loc['B'])

# DataFrame with hierarchical indexing
df = pd.DataFrame(
    {'Value': [1, 2, 3, 4]},
    index=pd.MultiIndex.from_tuples(
        [('A', 'X'), ('A', 'Y'), ('B', 'X'), ('B', 'Y')],
        names=['Group', 'Label']
    )
)
print("\nHierarchical DataFrame:")
print(df)

# Accessing hierarchical DataFrame
print("\ndf.loc['A', 'X']:\n", df.loc['A', 'X'])
print("\ndf.loc['A']:\n", df.loc['A'])
print("\ndf['Value']:\n", df['Value'])
