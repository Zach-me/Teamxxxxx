#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   demo01.py
@Time    :   2023/10/28 10:49:18
@Author  :   matrix 
@Version :   1.0
@Desc    :   查询 python 中的保留字
'''

def base():
    counter = 100 # 整型变量
    miles = 1000.0  # 浮点型变量
    name = "runoob"  # 字符串

    print (counter)
    print (miles)
    print (name)
    pass

def number():
    # 多个变量赋值
    a = b = c = 1
    a, b, c = 1, 2, '3'
    # Number（数字）
    # 支持 int float bool complex
    a, b, c, d = 20, 5.5, True, 4+3j
    print(type(a), type(b), type(c), type(d))
    # <class 'int'> <class 'float'> <class 'bool'> <class 'complex'>
    # 还可以使用 isinstance() 来判断
    a = 111
    isinstance(a, int) # True
    # bool 是 int 的子类，bool 可以和数字相加
    print(c + 10)

def type_demo():
    # type 和 isinstance 的区别在于
    # - type() 不会认为子类是一种父类类型
    # - isinstace() 会认为子类是一种父类类型
    class A:
        pass
    class B(A):
        pass
    print(isinstance(A(), A))
    print(type(A()) == A)
    print(isinstance(B(), A))
    print(type(B()) == A)
a = True
print(str(a))

