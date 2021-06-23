import pandas as pd

df = pd.read_excel('summerdata.xlsx')

df['hour'] = df['period'].dt.hour

# 平均值
data1 = df.groupby('hour').mean()

# 标准差
data2 = df.groupby('hour').std()

data1.to_excel('summer_daily_hour_mean.xlsx')
data2.to_excel('summer_daily_hour_std.xlsx')