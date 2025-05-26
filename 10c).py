import pandas as pd 
import numpy as np

df = pd.DataFrame({
    'Price': [100, 150, 200],
    'Tax': [10, 15, 20]
})

print("\nDataFrame:")
print(df)

# Arithmetic: Add a new column
df['total'] = df['Price'] + df['Tax']
print("\nAfter arithmetic operations (Price + Tax):")
print(df)

# Boolean Filtering
print("\nBoolean Filtering (total > 160):")
print(df[df['total'] > 160])
