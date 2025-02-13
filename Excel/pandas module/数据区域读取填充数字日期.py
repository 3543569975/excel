import pandas as pd
from datetime import date,timedelta

read = pd.read_excel('data.xlsx',sheet_name='2',skiprows=1,usecols='B:F',index_col = None,
                     dtype = {'id':str,'data':str,'time':str})
def add_month(d,md):
    yd = md//12
    m = d.month + md%12
    if m!=12:
        yd +=m//12
        m = m%12
    return date(d.year + yd,m,d.day)
start = date(2018,1,1)
for i in read.index:
    read['id'].at[i] = i+1
    read['data'].at[i] = 'a' if i%2==0 else 'b'
    read['time'].at[i] = add_month(start,i)  #start + timedelta(days=i)  //  date(start.year+i,start.month,start.day)

print(read)
read.set_index('Unnamed: 1',inplace = True)
read.to_excel('data1.xlsx')