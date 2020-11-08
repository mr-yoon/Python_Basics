"""
循环中可以和else配合循环使用，当循环正常结束之后要执行的代码

语法:
while：
    条件成立重复的代买
else：
    循环正常完成后执行的代码
"""

i = 1
while i <= 5:
    if i == 3:
        print("你说的不真诚")
        break
    print("我做错了")
    i += 1
else:
    print('谢谢你的原谅 ')