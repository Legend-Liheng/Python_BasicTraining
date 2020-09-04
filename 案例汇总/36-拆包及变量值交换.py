# -*- encoding: utf-8 -*-
"""
@File    : 36-拆包.py
@Time    : 2020/8/13 17:24
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

#返回值拆包
def student_inf(name, age):
    new_name = '名字是：%s' % name
    new_age = '年龄是：%d' % age

    return (new_name, new_age)#可不加括号，默认元组

ret = student_inf('李恒', 18)
name, age = ret#这就是拆包

print(name)
print(age)

#交换a、b的值
a, b = 4, 5
b, a = a, b

print('a = %d, b = %d' % (a, b))


