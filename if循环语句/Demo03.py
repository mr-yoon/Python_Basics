"""
-----猜拳游戏-----

需求分析:
    1、出拳：
        玩家：手动输入
        电脑：随机出拳
    2、判断输赢
        2.1：玩家获胜
        2.2：平局
        2.3：电脑获胜
"""

import random

# 1、玩家出拳动作
player = int(input("请出拳（0：石头，1：剪刀，2：布）："))
# 2、电脑随机出拳
computer_player = random.randint(0, 2)
print(computer_player)
# 3、判断输赢
if ((player == 0) and (computer_player == 1)) or \
        ((player == 1) and (computer_player == 2)) or \
        ((player == 2) and (computer_player == 0)):
    print(f'玩家获胜')
elif player == computer_player:
    print(f'平局')
else:
    print(f'电脑获胜')
