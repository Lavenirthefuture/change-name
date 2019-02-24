# -*- coding: UTF-8 -*-

import os, sys

# 打开文件
path = "D:/聆听音乐"
dirs = os.listdir(path)

# 输出所有文件和文件夹
for file in dirs:
    print(file)
    # print(file.find("C"))
    num = file.find("C")
    list_name = "聆听音乐-" + file[num - 3:num - 1]+".rmvb"
    print(list_name)
    os.rename(path + '/' + file, path + '/' + list_name)

# str1 = "this is really a string example....wow!!!"
# str2 = "is"
# print(str1.find(str2))
