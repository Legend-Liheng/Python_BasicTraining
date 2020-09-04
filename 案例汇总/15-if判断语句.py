# -*- encoding: utf-8 -*-
"""
@File    : 15-if判断语句.py
@Time    : 2020/8/4 20:22
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

my_age = int(input("请输入你的年龄："))

if my_age < 18:
    print("你是青少年!")
elif my_age < 40:
    print("你是壮年")
else:
    print("你是中老年")
