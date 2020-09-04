# -*- encoding: utf-8 -*-
"""
@File    : custom_sum.py
@Time    : 2020/8/28 13:44
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

name = '李恒'

def sum(a, b):
    return a + b

class Person():
    def eat(self):
        print('吃饭')

# if __name__ == '__main__':
#     pass

def main():
    print(name)

    print(sum(20, 30))

    Person().eat()

# print(__name__)
# print('哈哈，导入后会自动运行')

if __name__ == '__main__':
    main()
