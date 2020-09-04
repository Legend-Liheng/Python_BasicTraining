# -*- encoding: utf-8 -*-
"""
@File    : 11-输入.py
@Time    : 2020/8/4 8:42
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

import time

myName = input("请输入你的姓名：")
myQQ = input("请输入你的QQ号：")
myTel = input("请输入你的手机号：")
myAddress = input("请输入你的地址：")

print("名片信息生成中，请稍等……\n")
time.sleep(2)

print("-----------名片信息-----------")
print("姓名：%s" % myName)
print("QQ：%s" % myQQ)
print("手机号：%s" % myTel)
print("地址：%s" % myAddress)
print("----------------------------")