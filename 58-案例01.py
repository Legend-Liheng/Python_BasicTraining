# -*- encoding: utf-8 -*-
"""
@File    : 58-案例01.py
@Time    : 2020/9/3 15:29
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

"""
定义一个学生类。有下面的对象属性： 
姓名 
年龄 
成绩（语文，数学，英语)[每课成绩的类型为整数] 
对象方法： 
获取学生的姓名：get_name() 返回类型:str 
获取学生的年龄：get_age() 返回类型:int 
返回3门科目中最高的分数。get_course() 返回类型:int 
写好类以后，可以定义2个同学测试下: 

xm = Student('zhangming',22,[88,64,99]) 
返回结果： 
小明
22 
99 
"""

class Student():

    def __init__(self, name, age, scores_list):
        """
        :param name: 姓名
        :param age: 年龄
        :param scores_list:成绩列表
        """
        self.name = name
        self.age = age
        self.scores_list = scores_list

    # 获取学生姓名
    def get_name(self):
        return self.name

    # 获取学生年龄
    def get_age(self):
        return self.age

    # 获取3门科目中最高的成绩
    def get_max_scores(self):

        # self.scores_list.sort(reverse = True)
        # return self.scores_list[0]

        # python内置函数
        self.max_scores = max(self.scores_list)

        return self.max_scores

    def print_info(self):
        # self.get_name()
        # self.get_age()
        # self.get_max_scores()
        return self.get_name(), self.get_age(), self.get_max_scores()

    def __str__(self):
        return ('名字：%s 年龄：%d 最高成绩：%d' % (self.name, self.age, self.max_scores))

xiaoming = Student('小明', 18, [65, 50, 90])

print(xiaoming.get_name())
print(xiaoming.get_age())
print(xiaoming.get_max_scores())

# 调用__str__方法，打印属性值
print(xiaoming)

print(xiaoming.print_info())

xm_name, xm_age, xm_scores = xiaoming.print_info()
print(xm_name, xm_age, xm_scores)