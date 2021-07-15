import pandas as pd

df = pd.read_excel('111.xlsx')
df.set_index('period',inplace=True)

period1 = pd.date_range(start='2020-03-01 00:00:00',end='2021-02-28 23:55:00',freq='5min')
df_temp = pd.DataFrame(index=period1)

data = pd.concat([df_temp,df],axis=1)
data['period1'] = period1
# 查看缺失值
# print(data[data['CH4_dry'].isnull()])

# 年月日的加和作为分类依据1
day_number = data['period1'].dt.strftime("%Y-%m-%d")
data['day_number'] = day_number

# 小时作为分类依据2
data['hour'] = data['period1'].dt.hour

data_mean = data.groupby(['day_number','hour'])['CH4_dry'].mean()
data_std = data.groupby(['day_number','hour'])['CH4_dry'].std()
data_upper = data_mean + 3*data_std
data_lower = data_mean - 3*data_std

# 为每行数据填充上限值与下限值
data_upper_list = [val for val in data_upper for i in range(12)]
data_lower_list = [val2 for val2 in data_lower for n in range(12)]

data['lower'] = data_lower_list
data['upper'] = data_upper_list
data['True value'] = (data['CH4_dry']>=data['lower'])&(data['CH4_dry']<=data['upper'])

data.to_excel('finally_111.xlsx')