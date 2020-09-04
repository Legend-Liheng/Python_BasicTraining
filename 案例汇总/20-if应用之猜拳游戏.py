# -*- encoding: utf-8 -*-
"""
@File    : 20-if应用之猜拳游戏.py
@Time    : 2020/8/4 21:48
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

import random

print("下面开始猜拳游戏，规则如下：")
print("剪刀（0）石头（1）布（2）")

player = int(input("请输入："))

computer = random.randint(0, 2)

while (player <= 2) and (player >= 0):
    if player == 0:
        print("你输入的是剪刀")
        break
    elif player == 1:
        print("你输入的是石头")
        break
    elif player == 2:
        print("你输入的是布")
        break
else:
    print("你输入的不合法，请重新输入！")

if computer == 0:
    print("电脑输入的是剪刀")
elif computer == 1:
    print("电脑输入的是石头")
elif computer == 2:
    print("电脑输入的是布")

if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
    print("你赢了！")
elif (player == computer):
    print("你和电脑平局！")
else:
    print("电脑赢了！")
