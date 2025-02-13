import pandas as pd

df = pd.DataFrame({'id':[1,2,3],'name':['Tim','Bob','Nick']})
df = df.set_index('id')
df.to_excel('创建.xlsx')

