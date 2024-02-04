#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   index.py
@Time    :   2023/11/05 08:06:09
@Author  :   matrix 
@Version :   1.0
@Desc    :   None
'''
import json


info = """
**********************
1. 新增学生信息
2. 查询全部信息
3. 查询学生信息
4. 删除学生信息
5. 修改学生信息

0. 退出系统
**********************
"""

with open('sutdent.json', mode='r', encoding='utf-8') as f:
    text = f.read()
students = json.loads(text)

# students = [
#     {'name': '张三', 'math': 65, 'chinese': 65, 'english': 65, 'total': 195},
#     {'name': '李四', 'math': 100, 'chinese': 100, 'english': 100, 'total': 300}
# ]

while True:
    print(info)
    action = input("请选择你想要进行的操作：")
    if action == '1':
        print("新增学生信息")
        name = input("请输入学生姓名：")
        math = int(input("请输入数学成绩："))
        chinese = int(input("请输入语文成绩："))
        english = int(input("请输入英语成绩："))

        total = math + chinese + english
        students.append(
            {'name': name, 'math': math, 'chinese': chinese, 'english': english, 'total': total}
        )

    elif action == '2':
        # print("查询全部信息")
        print('姓名\t\t数学\t\t语文\t\t英语\t\t总分')
        for student in students:
            print('{}\t\t{}\t\t{}\t\t{}\t\t{}'.format(*student.values()))
    elif action == '3':
        # print("查询学生信息")
        name = input("请输入你想查询的学生姓名：")
        print('姓名\t\t数学\t\t语文\t\t英语\t\t总分')
        search_result = False
        for student in students:
            if student['name'] == name:
                print('{}\t\t{}\t\t{}\t\t{}\t\t{}'.format(*student.values()))
                search_result = True
                break
        if search_result:
            print(f'{name}这个学生不存在')

    elif action == '4':
        # print("删除学生信息")
        name = input("请输入要删除的学生姓名：")
        for student in students:
            if student['name'] == name:
                # students.pop(students.index(student))
                # students.remove(student)
                del students[students.index(student)]
                break
        else:
            print(f'{name}这个学生不存在')

    elif action == '5':
        # print("修改学生信息")
        name = input("请输入要修改的学生姓名：")
        for student in students:
            if student['name'] == name:
                math = int(input("请输入新的数学成绩："))
                chinese = int(input("请输入新的语文成绩："))
                english = int(input("请输入新的英语成绩："))
                total = math + chinese + english

                students[students.index(student)] = {'name': name, 'math': math, 'chinese': chinese, 'english': english, 'total': total}
        else:
            print(f'{name}这个学生不存在')
    elif action == '0':
        print("退出系统")
        with open('sutdent.json', mode='w', encoding='utf-8') as f:
            f.write(json.dumps(students, ensure_ascii=False))
        break
    else: 
        print("重新输入")
