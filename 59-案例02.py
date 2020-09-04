# -*- encoding: utf-8 -*-
"""
@File    : 59-案例02.py
@Time    : 2020/9/4 14:06
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

"""
一共有10名老师
老师 分别有  名字 年龄 性别 这些特征
罗元, 王梦涵,刘子怡,孙长胜,张成基 张志远,徐广来,张一山,王海, 陈阳
22, 26, 21, 26, 27, 33, 29, 44, 29, 31
"男", "女", "女", "男", "男", "男", "男", "男", "男", "男"
把这些老师保存到列表中
"""
class Main():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        return ('姓名：%s 年龄：%d 性别：%s' % (self.name, self.age, self.sex))

class Teacher():

    def __init__(self, ):
        self.name_list = ["罗元", "王梦涵", "刘子怡", "孙长胜", "张成基", "张志远", "徐广来", "张一山", "王海", "陈阳"]
        self.age_list = [22, 26, 21, 26, 27, 33, 29, 44, 29, 31]
        self.sex_list = ["男", "女", "女", "男", "男", "男", "男", "男", "男", "男"]

    def get_teacher_info(self):
        # 定义一个教师列表，用来保存教师信息
        teacher_list = []

        # 遍历获取教师信息
        for i, j in enumerate(self.name_list):
            self.name = self.name_list[i]
            self.age = self.age_list[i]
            self.sex = self.sex_list[i]

            # info = (self.name, self.age, self.sex)
            info = Main(self.name, self.age, self.sex)

            teacher_list.append(info)
        return teacher_list

techer = Teacher()

techers = techer.get_teacher_info()
for i in techers:
    print(i)