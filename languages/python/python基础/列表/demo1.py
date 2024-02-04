#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   demo1.py
@Time    :   2023/09/29 08:14:25
@Author  :   matrix 
@Version :   1.0
@Desc    :   列表的使用
'''

# 列表存储的是多个对象的引用，变量存储的是一个变量的引用
arr = [1, 2, 3, 4, 5, 6]

# 列表的切片，step 步长默认是 1 ， 如果超过或等于要切片的数据长度，则一直返回第一个元素
list1 = arr[1:4:1]

# 切片后的列表为新列表
print(list1)
print(id(arr))

# start = 6 stop  省略 step = -1
print(arr[6::-1])

print(1 in list1)
# 添加
# arr.append(100)
# arr.extend(1)
# arr.insert(2,10)
# print(arr)


# 删除
# arr.pop(-1)
# print(arr)

# 清空
# arr.clear()
# print(arr)

# 删除列表
# del arr
print(type(arr))

# 排序
arr.sort(reverse=True)
print(arr)
