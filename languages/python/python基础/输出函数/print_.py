# 可以输出数字
print(520)
print(12.34)

# 可以输出字符串
print('helloworld')
print("helloworld")

# 含有运算符的表达式
print(3+1)

# 将数据输出到文件中
fp = open('./text.txt', 'a+') # a+ 文件不存在则创建，存在则追加
print('helloworld', file=fp)
fp.close()

# 不进行换行输出（输出内容再一行当中）
print('hello', 'world', 'Python')

# 在同一行显示多条语句
import sys; x = 'test'; sys.stdout.write(x + '\n')
