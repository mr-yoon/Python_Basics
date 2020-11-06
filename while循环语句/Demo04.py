"""
学习目标:
    While语法（***）
    循环通常有for循环和while循环

    While循环语法
    while 条件:
        条件成立重复执行的代码1
        条件成立重复执行的代码2
        ......
"""

# 简单的循环语句实现方式
num = 1
while 5 >= num:
    print("我错了")
    num += 1
print("原谅你了")

# 计算1-100累加法

num = 1
sum = 0
while num <= 100:
    sum += num
    num += 1
print(sum)

# 计算1-100偶数累加和  ---------方法一
num = 1
sum = 0
while num <= 100:
    if num % 2 == 0:
        sum += num
    num += 1
print(f'1-100中偶数之和为：{sum}')

# 计算1-100偶数累加和  ---------方法一
num = 0
sum = 0
while num <= 100:
    sum += num
    num += 2
print(f'1-100中偶数之和为:{sum}')

"""
break 和 continue 退出循环
一：break
    当某些条件成立，终止整个循环过程
    

"""

# 吃苹果问题，当我吃到第三个的时候饱了输出结果
# 使用break输出--------
i = 1
sum = 0
while i <= 5:
    if i > 3:
        print("吃饱了，不吃了",end = '\n\n')
        break
    print(f'吃了第{i}个苹果')
    i += 1

# 使用continue输出-------
i = 1
sum = 0
while i <= 5:
    if i == 3:
        print(f'第{i}个苹果有虫子，不能吃')
        i += 1
        # 在使用continue时候，需要在执行之前修改计数器，否则会出现死循环
        continue

    print(f'吃了第{i}个苹果')
    i += 1


