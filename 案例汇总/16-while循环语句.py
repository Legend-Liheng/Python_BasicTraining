# -*- encoding: utf-8 -*-
"""
@File    : 16-while循环语句.py
@Time    : 2020/8/4 20:48
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""
import time

a = 0

#while循环语句，当while条件一直符合时，会循环执行
while a < 1:
    money = int(input("请投币："))

    if money >= 2:
        print("请上车……")
        time.sleep(2)
        seat = int(input("请输入当前剩余座位数量："))
        if seat == 0:
            print("没有座位，请站好！")
        else:
            print("有座位，请入座！")
    else:
        print("余额不足，请充值！")
    a += 1

print("\n循环结束！")


"""
    计算1~100的累计和
"""

num = 1
my_sum = 0

while num <= 100:

    my_sum += num
    num += 1

print("1~100的累计和为：", my_sum)


"""
    计算1~100之间的偶数之和
"""
num = 1
sum = 0

while num <= 100:

    if num % 2 == 0:
        sum += num

    num += 1
else:
    print("1~100之间的偶数和为：", sum)



