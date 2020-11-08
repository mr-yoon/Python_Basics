"""
字符串的常用方法:
下标:又称索引，能够通过下标快速定位元素内容s
切片
常用方法
"""

# 数据在程序运行过程中存在内存中

# 切片的语法内容： 变量名[开始节点下标 : 结束节点下标 ：间距（默认为1）]
# 下标默认选取为左开右闭  [ 开始下标 ： 结束下标 ）
# 默认不写开始位置下标，默认从0开始；如果不写结束，表示选取到最后；开始和结束都不写，表示选取所有
# 若以复数开始，下标为-1时，表示从最后一个元素开始

str1 = '1234567890'
print(str1[0: 9: 2])
print(str1[:3])
print(str1[:])
print(str1[::-1])

# 步长-1从右往方向发生冲突，无法选取数据
print(str1[-4:-1:-1])

print(str1[-1:-4:-1])
print("-------------------------------------", end="\n\n")
"""
字符串的常用方法：
1、查找 ；2、修改 、3：判断

1、查找（查找子串在字符串中的位置或者次数）
    find()：检查某个子串是否存在这个字符串中，如果在返回下标，不在返回-1
        语法： 字符串序列.find( 子串，开始位置下标 ，结束位置下标 )
    index()：检查某个子串是否存在这个字符串中，如果在返回下标，不在报错显示
        语法： 字符串序列.index( 子串，开始位置下标 ，结束位置下标 )
    count()：返回某个子串在字符串中出现的次数
        语法： 字符串序列.count( 子串，开始位置下标 ，结束位置下标 )
    rfind()、rindex()函数方法与find()和index()相同，只是查找顺序从右到左
    
"""

str2 = 'abcdefghijk'
mystr = 'hello world and java and python'

# find()函数
print(mystr.find('and', 0, len(mystr)))
print(mystr.find('ands', 0, len(mystr)))


# index()函数
print(mystr.index('and', 0, len(mystr)))
'''print(mystr.index('ands', 0, len(mystr)))'''

# count()函数
print(mystr.count('and', 0, len(mystr)))

print("-------------------------------------", end="\n\n")

"""
修改字符串
    replace()：替换作用
        语法：字符串序列.replace(旧子串 ， 新子串 ，替换次数)
        如果查出了子串出现次数，则替换次数为该子串的出现次数
        replace函数有返回值，不会修改原有的字符串内容，属于不可变类型
    split():按指定字符分割字符串
        语法：字符串序列.split(分割字符 ，num) num：表示分割字符出现次数
    join():将多个字符串合并为一个新的字符串
        语法：字符或子串.join(多字符串组成的序列)
    
    
"""
mystr = 'hello world and itcast and itheima and python'

# replace()函数
new_atr = mystr.replace('and', 'he')
print(new_atr)
print(mystr)

# split() 返回列表 (分割过程会丢失分割字符)
list1 = mystr.split('and', 2)
print(list1)

# join()合并字符串
mystr2 = ['aa', 'bb', 'cc']
new_list = '***'.join(mystr2)
print(new_list)
print("-------------------------------------", end="\n\n")

"""
字符串转换大小写方式
# capitalize():将字符串第一个字符转换成大写
# title()：将字符串转换为大写
# lower()：将字符串转为小写
# upper():将字符串转为小写转为大写
"""

mystr = 'hello world and itcast and itheima and python'

new_str = mystr.capitalize()
print(new_str)

new_str1 = mystr.title()
print(new_str1)

new_str2 = mystr.lower()
print(new_str2)

new_str3 = mystr.upper()
print(new_str3)

print("-------------------------------------", end="\n\n")


"""
lstrip():删除字符串左侧空白字符
rstrip():删除字符串右侧空白字符
strip():删除字符串两侧空白字符
"""

mystr = '   hello world and itcast and itheima and python   '

new_list = mystr.rstrip()
new_list1 = mystr.lstrip()
new_list2 = mystr.strip()
print(mystr)
print(new_list)
print(new_list1)
print(new_list2)

print("-------------------------------------", end="\n\n")


"""
ljust():返回一个原字符串左对齐，并使用指定字符（默认为空）填充对应长度
    语法：字符串序列.ljust（长度，填充字符）
ljust():删除字符串右侧空白字符

just():删除字符串两侧空白字符
"""

mystr = 'hello'
new = mystr.ljust(10, '*')
new1 = mystr.rjust(10, '`')
new2 = mystr.center(10, '&')
print(new)
print(new1)
print(new2)

print("-------------------------------------", end="\n\n")


