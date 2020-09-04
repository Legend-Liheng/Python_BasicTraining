# -*- encoding: utf-8 -*-
"""
@File    : 07-格式化输出.py
@Time    : 2020/8/3 22:07
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

"""
    实际应用中不需要标注
    可以直接输出结果
    除非想转换数据类型
"""


#字符串类型
my_name = '李恒'
print("我的名字:%s" % my_name)
print(my_name)

#整型
my_age = 28
print("我的年龄:%i" % my_age)
print(my_age)

#浮点型
my_height = 166.66666
print("我的身高:%0.2f" % my_height)
print(my_height)

#布尔类型
is_man = True
print("我的性别:%s" % is_man)
print(is_man)
