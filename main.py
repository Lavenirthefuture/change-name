# -*- coding: UTF-8 -*-

import os, sys

# 打开文件
path = "J:/剧/瑞克和莫迪/瑞克 一般"
dirs = os.listdir(path)
letter = "S"


# 输出所有文件和文件夹
for file in dirs:
    print(file)
    # print(file.find("C"))
    num = file.find(letter)
    list_name = "R&M " + file[num:num+6] + file[file.rfind("."):]
    print(list_name)
    os.rename(path + '/' + file, path + '/' + list_name)

# str1 = "this is really a string example....wow!!!"
# str2 = "is"
# print(str1.find(str2))
