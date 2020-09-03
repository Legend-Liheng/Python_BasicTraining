# -*- encoding: utf-8 -*-
"""
@File    : 47-继承.py
@Time    : 2020/8/26 20:19
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""


class Mater(object):
    def __init__(self):
        self.kongfu = '煎饼果子古老配方'

    def make_cake(self):
        print('使用{%s}制作煎饼果子' % self.kongfu)

    def user_wood(self):
        print('使用木柴作为火源')

#只继承一个父类，称之为单继承
class Disciple1(Mater):
    pass

# xiaoma = Disciple1()
# xiaoma.make_cake()

class School(object):
    def __init__(self):
        self.kongfu = '煎饼果子现代配方'

    def make_cake(self):
        print('使用{%s}制作煎饼果子' % self.kongfu)

    def user_oil(self):
        print('使用油作为火源')

class Disciple2(Mater, School):
    pass

xiaozhang = Disciple2()

#多继承中，当调用的方法在两个父类中都存在，那么调用第一个父类中的方法
# xiaozhang.make_cake()
#
# #当调用的方法只存在一个父类中时，分别调用
# xiaozhang.user_wood()
# xiaozhang.user_oil()

class Disciple3(Mater, School):

    def __init__(self):
        self.kongfu = '融合后的配方'

    #子类继承父类后，重写方法、属性，做自己的事情
    def make_cake(self):
        print('使用｛%s｝制作煎饼果子' % self.kongfu)

    #子类调用父类同名方法和属性
    def make_old_cake(self):
        # print('古法配方：%s' % Mater().kongfu)
        Mater.make_cake(self)#类调用方法
        Mater().make_cake()#实例调用方法
        super(Mater, self).make_cake()
        super().make_cake()

    def make_new_cake(self):
        # print('现代配方：%s' % School().kongfu)
        School().make_cake()

xiaoli = Disciple3()
#对象调用方法，先从子类中找，找到后会执行，没找到再去父类中找
# xiaoli.make_cake()

xiaoli.make_old_cake()
# xiaoli.make_new_cake()