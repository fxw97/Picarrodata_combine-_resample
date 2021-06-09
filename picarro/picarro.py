import pandas as pd
import glob

files = glob.glob('20200502/*.dat')

data_all = pd.DataFrame()
for file in files:
    data = pd.read_table(file)
    head = data.columns.values
    list_columns_temp = head[0].split(' ')
    list_columns = [x for x in list_columns_temp if x !='']

    list_all = []
    for n in data.values:
        list_temp = n[0].split(' ')
        list = [x for x in list_temp if x !='']
        list_all.append(list)

    data_final = pd.DataFrame(list_all,columns=list_columns,index=None)
    data_final['period'] = data_final['DATE']+' '+data_final['TIME']
    data_final.drop(columns=['DATE','TIME'],inplace=True)
    data_final['period'] = pd.to_datetime(data_final['period'])
    data_final.set_index('period',inplace=True)
    data_final.loc[:,'FRAC_DAYS_SINCE_JAN1':'nh3_conc_ave'] = data_final.loc[:,'FRAC_DAYS_SINCE_JAN1':'nh3_conc_ave'].apply(pd.to_numeric)
    data_final = data_final.resample('5min').mean()
    data_all = pd.concat([data_all,data_final])

data_all.to_excel('picarro-20200502-5mindata.xlsx')