# 1.导入pandas模块
import pandas as pd
#import pygwalker as pyg
'''
# 2.把Excel文件中的数据读入pandas
df = pd.read_excel('data.xlsx')
print(df)

# 3.读取excel的某一个sheet
df = pd.read_excel('data.xlsx', sheet_name='2')
print(df)
gwalker = pyg.walk(df)
# 4.获取列标题
print('列标题:')
print(df.columns)
# 5.获取行标题
print('行标题:')
print(df.index)
# 6.制定打印某一列
print('打印1b列')
print(df["1b"])
# 7.描述数据
print('描述数据')
print(df.describe())
# 8.excel的行列总数
print('行列总数')
print(df.shape)
# 9.ececl的3行（默认为5）,head前, tail后
print(df.head(3))
print(df.tail(3))
'''
# 10.按行读取
data = pd.read_excel('data.xlsx',sheet_name = '2',usecols='A:C')
for index,row in data.iterrows():
    column1_value = row['3']
    column2_value = row['4']
print(column2_value)
'''
7.
对于数值型数据，
count：非空值的数量。
mean：所有数值的平均值。
std：标准差，是一个表示数据分散程度的指标。
min：最小值。
25%：第一四分位数，表示所有数值中25%的数据低于这个值。
50%：中位数，表示所有数值排序后的中间值，50%的数据低于这个值，50%的数据高于这个值。也被称为第二四分位数。
75%：第三四分位数，表示所有数值中75%的数据低于这个值。
max：最大值。
对于非数值型数据，
count（非空值的数量）
unique（唯一值的数量）
top（出现最多的值）
freq（最常见的值出现的频率）
'''
