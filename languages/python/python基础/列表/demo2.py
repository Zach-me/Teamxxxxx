#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   demo2.py
@Time    :   2023/09/29 08:57:16
@Author  :   matrix 
@Version :   1.0
@Desc    :   None
'''

# 列表生成式
arr = [i*i for i in range(1,10)]
print(arr)

arr2 = [11,12,13,14]
# 原地修改，修改的值不会赋值给arr3，会赋值None
arr3 = arr.extend(arr2)

print(arr)
