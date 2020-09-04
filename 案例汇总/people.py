# -*- encoding: utf-8 -*-
"""
@File    : people.py
@Time    : 2020/9/4 16:20
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

class People(object):

    def __init__(self, name, sex, age, nationality):
        '''
        :param name:姓名
        :param sex:性别
        :param age:年龄
        :param nationality:国籍
        '''
        self.name = name
        self.sex = sex
        self.age = age
        self.nationlity = nationality

    def eat(self):
        print('吃饭')

    def sleep(self):
        print('睡觉')

    def work(self):
        print('工作')

    def __str__(self):
        return ('姓名：%s 性别：%s 年龄：%d 国籍：%s' % (self.name, self.sex, self.age, self.nationlity))

