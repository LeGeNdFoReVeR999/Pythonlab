import pandas as pd
import matplotlib.pyplot as plt

data={
    'Math':[90,80,75,60],
    'Physics':[85,78,92,70],
    'Chemistry':[88,76,94,82]
}
index=pd.MultiIndex.from_tuples([('Alice','2023'),('Alice','2024'),('Bob','2023'),('Bob','2024')],names=['Student','Year'])
df=pd.DataFrame(data,index=index)
df['Math'].plot(kind='bar',title='MathScores')
plt.xlabel('Student_year')
plt.ylabel('Score')
plt.tight_layout()
plt.show()
df[['Math','Physics','Chemistry']].plot(kind='line',title='Subject Scores')
plt.xlabel('Student_year')
plt.ylabel('Score')
plt.tight_layout()
plt.show()