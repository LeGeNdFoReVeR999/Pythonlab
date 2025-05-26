import pandas as pd

data={
    'Math':[90,80,75,60],
    'Physics':[85,78,92,70],
    'Chemistry':[88,76,94,82]
}
index=pd.MultiIndex.from_tuples([('Alice','2023'),('Alice','2024'),('Bob','2023'),('Bob','2024')],names=['Student','Year'])
df=pd.DataFrame(data,index=index)
df.to_csv('Student_Scores.csv')
print('Data written to Student_Scores.csv')
read_df=pd.read_csv('Student_scores.csv',index_col=[0,1])
print("\nData read from csv:\n",read_df)