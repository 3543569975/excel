import os

folder_path = os.path.join('C:\\Users\\l\\OneDrive\\桌面\\L\\pycharm\\pycharm练习\\Excel\\Excel\\os模块\\表格')

for name in os.listdir(folder_path):
    file_path = os.path.join(folder_path,name)
    print(file_path)
for name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, name)
    f = open(file_path,'r')#(csv文件不用utf-8)
    data = f.read()
    f.close()
    print(file_path,'=====',data)