# -*- encoding: utf-8 -*-
"""
@File    : 09-换行输出.py
@Time    : 2020/8/4 8:28
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

print("你好，世界")

#\n为换行符，等同于键盘中的回车键
print("你好\n世界")

num1 = 20
num2 = 4
num3 = num1/num2

print("%d/%d = %d"%(num1, num2, num3))

#单纯的一个百分号%需要输入两个%%进行换算显示
num = 98
print("成活率达到了%d%%" % num)