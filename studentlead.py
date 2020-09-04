# -*- encoding: utf-8 -*-
"""
@File    : studentlead.py
@Time    : 2020/9/4 16:21
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""
from student import Student

class StudentLead(Student):

    def __init__(self, name, sex, age, nationality, school, num, position):
        super().__init__(name, sex, age, nationality, school, num)
        self.position = position

    def meet(self):
        print('开会')

    def __str__(self):
        return ('姓名：%s 性别：%s 年龄：%d 国籍：%s 学校：%s 学号：%d 职位：%s' % (self.name, self.sex, self.age, self.nationlity, self.school, self.num, self.position))
