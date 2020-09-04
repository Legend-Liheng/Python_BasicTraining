# -*- encoding: utf-8 -*-
"""
@File    : student.py
@Time    : 2020/9/4 16:20
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""
from people import People

class Student(People):

    def __init__(self, name, sex, age, nationality, school, num):
        # 继承父类的__init__方法
        super().__init__(name, sex, age, nationality)
        self.school = school
        self.num = num

    def work(self):
        print('上学')

    def __str__(self):
        return ('姓名：%s 性别：%s 年龄：%d 国籍：%s 学校：%s 学号：%d' % (self.name, self.sex, self.age, self.nationlity, self.school, self.num))
