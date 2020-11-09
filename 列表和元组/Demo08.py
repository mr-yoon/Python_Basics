"""
列表可以一次性存储多个数据，且可以为不同数据类型

1、查找
    index():返回指定数据所在位置的下标
    count():指定数据在当前列表出现的次数
    len()：访问列表的长度

"""

name_list = ['tom', 'lilyaaaaa', 'rose']
print(name_list.index('tom'))
print(name_list.count('tom'))
print(len(name_list[1]))

"""
判断列表中的数据是否存在
    in 判断某数据是否在列表中
    not in 判断某数据是否不在列表中
"""
name_list = ['tom', 'lilyaaaaa', 'rose']
print('tom' in name_list)
print('t' not in name_list[0])
print("-----------------------------", end='\n\n')

name_list = ['tom', 'lilyaaaaa', 'rose']
name = 'tom'  # 'input("输入你的邮箱账号名:")
if name in name_list:
    print(f'你输入的名字是：{name},此用户名已经存在')
else:
    print(f'你输入的名字是：{name},可以注册')
print("-----------------------------", end='\n\n')

"""
增加数据
    append()：列表结尾追加数据
        语法：列表序列.append(元素)
    extend():列表结尾增加数据，如果列表是一个序列，则将这个序列的数据逐一添加到列表
    insert():指定位置新增数据
        语法：列表序列.insert(位置下标，数据)
"""

name_list = ['tom', 'lilyaaaaa', 'rose']
# 列表是一个可变的类型
# 如果append()追加的数据是一个序列，则将这个序列的数据逐一添加到列表中
name_list.append('xiaoming')
name_list.append([11, 12, 14])
print(name_list)

# extend()方法
name_list.extend([11, 12, 14])
print(name_list)

# insert() 函数
name_list = ['tom', 'zhansan']
name_list.insert(1, 'qinahng')
print(name_list.insert(1, 'wujiang'))  # insert()方法没有返回值，所以不成立
print(name_list)
print("-----------------------------", end='\n\n')
"""
6. 删除列表中的元素
	a. 方法一：
		i. 语法：del + 空格 + 变量名[索引]
		ii. 使用该方法的前提是我们要知道需要删除元素的索引；
	b. 方法二：
		i. 语法:变量名.pop（）。
		ii. pop（）方法可删除末尾的元素，并且支持让你能够接着使用它。
		iii. pop（索引）删除索引所在位置的元素。
		iv. 每使用pop（）弹出一个元素后，该元素将不存在与列表中了。
	c. 判断使用del还是pop（）方法删除元素
		i. 若从列表中删除后，将不再以任何方式使用它，使用del语句删除元素。
        删除该元素后，还能继续使用它，使用pop（）语法删除元素。

"""
names = ['zhang li', 'li rui', 'honda', 'su zhou']
del names[0]
print(names)

# 利用pop（）方法删除元素
names = ['zhang li', 'li rui', 'honda', 'su zhou']
print(names)
pop_names = names.pop()
# names列表中删除的元素存储在pop_names中
print(names)
print(pop_names)
pop_names = names.pop(1)
print(pop_names)
print(names)
print("-----------------------------", end='\n\n')

# remove(数据)
name_list = ['tom', 'lilyaaaaa', 'rose']
new_name = name_list.remove('tom')
print(name_list)
print(new_name)

print("-----------------------------", end='\n\n')

"""
修改列表
    
"""
# 修改指定下标的数据
name_list = ['tom', 'lilyaaaaa', 'rose']
name_list[0] = 'aa'
print(name_list)

# 逆序排序 severse()
list1 = [1, 2, 3, 4, 6, 8, 3]
list1.reverse()
print(list1)

# sort() 排序（升序、降序）
# 语法： 列表序列.sort(key = None, reverse = False)
# reverse表示排序规则，reverse = True降序， reverse = False升序
list1 = [1, 3, 5, 2, 9, 4, 6]
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)

print("-----------------------------", end='\n\n')

"""
复制数据
    copy()
"""
name_list = ['tom', 'lily', 'Rose']
name_list1 = name_list.copy()
print(name_list1)

print("-----------------------------", end='\n\n')