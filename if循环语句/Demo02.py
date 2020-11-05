# 判断时候能上车和有空座位
"""
1、判断是否有钱、有钱可以做公交车；
2、坐公交时候，判断是否有空座，有则坐下
"""

money = float(input("我口袋里有多少钱:"))
if money >= 1:
    print("有钱坐公交车")
    soat = float(input("我看到座位有："))
    # 判断是否有空座位
    if soat >= 1:
        print("有空座位")
    else:
        print("没有空座位")
else:
    print("not money")
print("结束本次活动")
