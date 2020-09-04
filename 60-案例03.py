# -*- encoding: utf-8 -*-
"""
@File    : 60-案例03.py
@Time    : 2020/9/4 14:37
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

'''
    定义一个人类，包括属性：姓名、性别、年龄(age)、国籍；
    包括方法：吃饭、睡觉，工作(work)。
    （1）根据人类，派生一个学生类，增加属性：学校、学号；重写工作方法（学生的工作是学习(study)）。
    （2）根据人类，派生一个工人类，增加属性：单位、工龄；重写工作方法（工人的工作是„„自己想吧）。
    （3）根据学生类，派生一个学生干部类，增加属性：职务；增加方法：开会。
    （4）编写主函数分别对上述3类具体人物进行测试。
'''
#
# class People():
#
#     def __init__(self, name, sex, age, nationality):
#         '''
#         :param name:姓名
#         :param sex:性别
#         :param age:年龄
#         :param nationality:国籍
#         '''
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.nationlity = nationality
#
#     def eat(self):
#         print('吃饭')
#
#     def sleep(self):
#         print('睡觉')
#
#     def work(self):
#         print('工作')
#
#     def __str__(self):
#         return ('姓名：%s 性别：%s 年龄：%d 国籍：%s' % (self.name, self.sex, self.age, self.nationlity))

# class Student(People):
#
#     def __init__(self, name, sex, age, nationality, school, num):
#         # 继承父类的__init__方法
#         super().__init__(name, sex, age, nationality)
#         self.school = school
#         self.num = num
#
#     def work(self):
#         print('上学')
#
#     def __str__(self):
#         return ('姓名：%s 性别：%s 年龄：%d 国籍：%s 学校：%s 学号：%d' % (self.name, self.sex, self.age, self.nationlity, self.school, self.num))

# class Workers(People):
#
#     def __init__(self, name, sex, age, nationality, unit, work_len):
#         super().__init__(name, sex, age, nationality)
#         self.unit = unit
#         self.work_len = work_len
#
#     def work(self):
#         print('工地工作')
#
#     def __str__(self):
#         return ('姓名：%s 性别：%s 年龄：%d 国籍：%s 单位：%s 工龄：%d' % (self.name, self.sex, self.age, self.nationlity, self.unit, self.work_len))

# class StudentLead(Student):
#
#     def __init__(self, name, sex, age, nationality, school, num, position):
#         super().__init__(name, sex, age, nationality, school, num)
#         self.position = position
#
#     def meet(self):
#         print('开会')
#
#     def __str__(self):
#         return ('姓名：%s 性别：%s 年龄：%d 国籍：%s 学校：%s 学号：%d 职位：%s' % (self.name, self.sex, self.age, self.nationlity, self.school, self.num, self.position))

# 接下来导入模块话的各类方法
from people import People
from student import Student
from workers import Workers
from studentlead import StudentLead

if __name__ == '__main__':

    people = People('人类', '未知', 10, '中国')

    print('以下为People类的数据')
    people.eat()
    people.sleep()
    people.work()
    print(people)

    print('---------------我是一条分隔线------------------')
    student = Student('学生', '未知', 18, '中国', '城西银泰', 1)

    print('以下为Student类的数据')
    student.work()
    print(student)

    print('---------------我是一条分隔线------------------')
    worker = Workers('工人', '男', 30, '中国', '小码王', 3)

    print('以下是Workers类的数据')
    worker.work()
    print(worker)

    print('---------------我是一条分隔线------------------')

    studentlead = StudentLead('学生干部', '女', 18, '中国', '城西银泰', 10, '学生会主席')

    print('以下是StudentLead类的数据')
    studentlead.meet()
    print(studentlead)


