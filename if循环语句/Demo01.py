"""
条件语句学习，
"""

# 条件成立则执行一个分支代码，条件不成立则不成立这些代码

"""
if 条件:
    条件成立执行的代码块1
    .......
"""

# 例子1
if True:
    print("条件成立执行的代码")

print("成不成立都执行代码", end='\n\n')

# 例子2
age = 18
if age >= 18:
    print("你可以上网了")

print("不想上网了", end='\n\n')

# 输入年龄，判断上网
age = int(input("请输入你自己的年龄"))
if age >= 18:
    print("你的年龄是%d，你可以上网了" % age)  # 使用%d
    print(f'你输入的年龄是{age},已经成年了，可以上网')

print("不想上网了", end='\n\n')

"""
   if...else...语法：

if 条件:
    条件成立执行代码
    条件成立执行代码
else：
    条件不成立执行代码
    条件不成立执行代码
"""

# 例子

age = int(input("请输入你的年龄:"))
if age >= 18:
    print(f'你的年龄{age}岁，可以上网')
else:
    print(f'你的年龄{age}岁，未成年，不可以上网')

print("不想上网了", end='\n\n')

'''
多重判断

if 条件:
    条件1成立执行代码
    条件2成立执行代码
elif:
    条件3成立执行代码
    条件4成立执行代码
else：
    条件5成立执行代码
'''

# 例子

age = int(input("请输入你的年龄："))

if age < 18:
    print(f'你输入的年龄是{age},属于童工')
elif 18 <= age <= 60:
    print(f'你输入的年龄是{age},正常工')
else:
    print(f'你输入的年龄是{age},退休年龄')

# 判断时候能上车和有空座位
"""
1、判断是否有钱、有钱可以做公交车；
2、坐公交时候，判断是否有空座，有则坐下
"""

money = float(input("我口袋里有多少钱:"))
if money >= 1:
    print("有钱坐公交车")
    soat = float(input("我看到座位有："))
    if soat >= 1:
        print("有空座位")
    else:
        print("没有空座位")

else:
    print("not money")
