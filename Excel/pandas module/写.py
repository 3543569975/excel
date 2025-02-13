import pandas as pd

s1 = pd.Series([1,2,3],index=[1,2,3],name='A')
s2 = pd.Series([10,20,30],index=[1,2,3],name='B')
s3 = pd.Series([100,200,300],index=[1,2,3],name='C')

df = pd.DataFrame({s1.name:s1,s2.name:s2,s3.name:s3})
print(df)

df1 = pd.DataFrame([s1,s2,s3])
print(df1)

ls = [1,2,3,4,5]
ls1= [10,20,30,40,50]
ls2 = [100,200,300,400,500]
s1 = pd.Series(ls)
s2 = pd.Series(ls1)
s3 = pd.Series(ls2)
df2 = pd.DataFrame([s1,s2,s3],)
df2 = df2.set_index(0)
df2 = df2.drop(10,axis=0)#删除索引为10的行，行0，列1
print(df2)


df2.to_excel('写.xlsx')