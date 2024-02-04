#!/bin/bash
# -*- coding: utf-8 -*-
#File    :   run.sh
#Time    :   2023/10/28 10:25:09
#Author  :   matrix 
#Version :   1.0
#Desc    :   None

#key point:
#1) data 命令的用法，可根据日期、时间获取到想要的字符
#2）for 循环如何遍历文件

# 定义后缀变量，注意这个``反引号的含义
suffix=`date +%Y%m%d`

# 找到 /data/ 目录下的 txt 文件，用 for 循环遍历
for f in `find ./data/ -type f -name "*.txt"`
do
    echo "备份文件$f"
    cp ${f} ${f}_${suffix}
done
