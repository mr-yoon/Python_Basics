"""
元组中的数据是不支持修改的
元组使用（数据1，数据2）表示
元组数据只支持查找；
"""

# 多个数据元组
t1 = (10, 12, 14)

# 单个数据元组
# ******单个数据的元组必须加“，”号，否则为该数据的数据类型
t2 = (12)
t3 = ('df')

print(type(t1))
print(type(t2))
print(type(t3))

# 元组中的数据不支持修改；但是若元组中有列表则列表数据支持修改
tuple1 = ('aa', 'bb', 'cc', 'dd')
tuple2 = (10, 12, 13, ['aa', 'bb', 'cc', 'dd'])
i = 0
while i < len(tuple2):
    print(tuple2[i])
    i += 1

tuple2[3][3] = 'sdfg'
print(tuple2[3][3])
print(tuple2)
