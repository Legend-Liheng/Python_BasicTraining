# -*- encoding: utf-8 -*-
"""
@File    : 45-类属性和类方法.py
@Time    : 2020/8/26 15:17
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

class Car():
    #在类中定义的属性，为类属性
    car_name = '宝马'
    car_num = 10

    #构造方法
    def __init__(self, name, age):
        self.person_name = name
        self.person_age = age
        Car.car_num += 1

    #实例方法
    def car_color(self):
        return '黑色'
        # return self.car_name

    #类方法
    @classmethod
    def car_age(cls):
        return cls.car_name

    #静态方法
    @staticmethod
    def say():
        print('我是一个静态方法')

    # __str__方法，在print(对象)时会自动打印出返回值
    def __str__(self):
        return '名字：%s 年龄：%d' % (self.person_name, self.person_age)

    # 折构方法，在对象销毁时会自动调用
    def __del__(self):
        print('对象已销毁！')

xiaoming = Car('小明', 20)

# 使用实例属性
print('修改前实例属性：' + xiaoming.person_name)

# 修改实例属性
xiaoming.person_name = '小红'
print('修改后实例属性：' + xiaoming.person_name)

# 使用类属性
print('对象名.类属性展示类属性：' + xiaoming.car_name)# 01：对象名.类属性
print('类名.类属性展示类属性：' + Car.car_name)# 02：类名.类属性

# 修改类属性
xiaoming.car_name = '奔驰'
print('修改类属性后')

# 在实例上修改类属性，实际上并没有修改，而是给实例绑定了一个实例属性
print('对象名.类属性展示类属性：' + xiaoming.car_name)
print('类名.类属性展示类属性：' + Car.car_name)

#调用实例方法
print(xiaoming.car_color())

#调用类方法
print(xiaoming.car_age())#通过对象调用类方法
print(Car.car_age())#通过类名调用类方法

#调用类属性
print(xiaoming.car_num)

#调用静态方法
xiaoming.say()
Car.say()

print(xiaoming)

