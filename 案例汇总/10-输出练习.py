# -*- encoding: utf-8 -*-
"""
@File    : 10-输出练习.py
@Time    : 2020/8/4 8:37
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

"""
    输出方式1：print("姓名：%s" % myName)
    输出方式2：print("姓名：", myName)【一般用这个】
"""
#姓名
myName = "李恒"

#QQ
myQQ = "13204744295"

#手机号
myTel = 18322828061

#地址
myAddress = "浙江省杭州市"

print("-----------我的名片信息-----------")
print("姓名：%s" % myName)
print("QQ：%s" % myQQ)
print("手机号：%d" % myTel)
print("地址：%s" % myAddress)
print("--------------------------------")



