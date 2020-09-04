# -*- encoding: utf-8 -*-
"""
@File    : workers.py
@Time    : 2020/9/4 16:21
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

from people import People

class Workers(People):

    def __init__(self, name, sex, age, nationality, unit, work_len):
        super().__init__(name, sex, age, nationality)
        self.unit = unit
        self.work_len = work_len

    def work(self):
        print('工地工作')

    def __str__(self):
        return ('姓名：%s 性别：%s 年龄：%d 国籍：%s 单位：%s 工龄：%d' % (self.name, self.sex, self.age, self.nationlity, self.unit, self.work_len))

# print('---------------我是一条分隔线------------------')
# worker = Workers('工人', '男', 30, '中国', '小码王', 3)
#
# print('以下是Workers类的数据')
# worker.work()
# print(worker)