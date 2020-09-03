# -*- encoding: utf-8 -*-
"""
@File    : 35-fadsf.py
@Time    : 2020/8/10 21:44
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

#多个return
def num_cal(a, b):
    if a > b:
        return a - b
    else:
        return a + b

print(num_cal(1, 2))

#-------------------------分隔线-----------------------
#返回多数据

# #返回列表样式
# def student_inf(name, age):
#     new_name = '名字是：%s' % name
#     new_age = '年龄是：%d' % age
#
#     return [new_name, new_age]
#
# ret = student_inf('李恒', 18)
# print(ret[0])
# print(ret[1])

#返回元组样式
def student_inf(name, age):
    new_name = '名字是：%s' % name
    new_age = '年龄是：%d' % age

    return (new_name, new_age)#可不加括号，默认元组

ret = student_inf('李恒', 18)
print(ret[0])
print(ret[1])

#返回字典格式
def student_inf(name, age):
    new_name = '名字是：%s' % name
    new_age = '年龄是：%d' % age

    return {'name': new_name, 'age': new_age}

ret = student_inf('李恒', 18)
print(ret['name'])
print(ret['age'])



