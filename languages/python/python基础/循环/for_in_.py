# 使用 for 循环，计算 1 到 100 之间的偶数和

sum = 0  # 用于存储偶数和
nums = []
for item in range(1,101):
    if item % 2 == 0:
        nums.append(item)  # 把加过的数都添加到列表中
        sum += item
print('1 到 100 之间的偶数和为', sum)
print('添加的数有:\n', nums)

# range(x,y) 左闭右开
for num in range(1,5):
    print("num",num)
