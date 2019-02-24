# -*- coding: UTF-8 -*-

import os, sys

# 打开文件
path = "D:/聆听音乐"
dirs = os.listdir(path)

# 输出所有文件和文件夹
for file in dirs:
    print(file)
    num = file.find(".rmvb")
    print(num)
    if num == -1:
        os.rename(path + '/' + file, path + '/' + file + '.rmvb')

    # os.rename(path + '/' + file, path + '/' + list_name)
