# -*- encoding: utf-8 -*-
"""
@File    : 08-常用的格式符号.py
@Time    : 2020/8/4 8:18
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

my_life = "c"
my_name = "李恒"
my_age = 28
my_height = 16.66666

print("字符输出：%c" % my_life)
print("字符串输出：%s" % my_name)
print("有符号十进制整数：%d" % my_age)
print("无符号十进制整数：%u" % my_age)
print("八进制整数：%o" % my_age)
print("十六进制整数（小写0x）：%x" % my_age)
print("十六进制整数（大写0X）：%X" % my_age)
print("浮点数：%f" % my_height)
print("科学计数法（小写e）：%e" % my_age)
print("科学计数法（大写E）：%E" % my_age)
print("简写%g" % my_age)  #%f和%e的简写
print("简写%G" % my_age)  #%f和%E的的简写

