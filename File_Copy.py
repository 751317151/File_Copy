import os
import time

st = time.time()
rootdir = '.\\'
list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
for i in range(0,len(list)):
    path = os.path.join(rootdir,list[i])
    if os.path.isfile(path):
        src = open(path, "rb") 
        dst = open("副本"+path[2:], "wb")   
        dst.write(src.read()) 

et = time.time()
at = et-st
n = len(list)
print("共拷贝了%s个文件"%n)
print("总用时为：%s秒"%at)
print("平均用时为：%s秒"%(at/n))
src.close() 
dst.close() 
