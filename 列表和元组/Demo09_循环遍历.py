# while循环实现遍历
name_list = ['tom', 'lily', 'Rose']
i = 0
while i < len(name_list):
    print(name_list[i])
    i += 1

# for循环实现遍历
name_list = ['tom', 'lily', 'Rose']
i = 0
for i in name_list:
    print(i)
print('---------------------------------------',end='\n\n')
"""
列表的嵌套
"""
name_list = [
    ['小明', '小红', '小绿'],
    ['Tom', 'lily', 'Rose'],
    ['张三', '李四', '王二'],
    ['jj', 'qq', 'kk']]
# 查找到第一个子列表的长度
print(len(name_list[0]))
# 打印小红
print(name_list[0][1])

# 案列-随机分配办公室
# 有三个办公室，8位老师，随机分配8位老师到三个办公室

"""
1、准备数据
    8位老师
    3个办公室
2、分配老师到办公室
    将老师的名字加到办公室列表
3、验证是否分配成功
    打印办公室信息
"""
import random

# 准备数据
offices = [[], [], []]
teachers = ['li', 'zhang',
           'wang', 'zhao',
           'zhou', 'yin',
           'huang', 'chou', ]

# 分配老师办公室
for name in teachers:
    # 列表追加数据
    # 随机生成0到2的整数
    num = random.randint(0, 2)
    offices[num].append(name)
# 验证是否成功
i = 1
for office in offices:
    print(f'办公室{i}的人数{len(office)},老师分别是:')
    for name in office:
        print(name)
    i += 1



