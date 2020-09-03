# -*- encoding: utf-8 -*-
"""
@File    : 05-命名规范.py
@Time    : 2020/8/3 22:00
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

#类名命名规范：驼峰命名法，首字母大写
class NameRules():
    #方法命名规范：小写，下划线连接
    def name_rules(self):
        #变量命名方法：连续小写
        myname = '李恒'
        return myname

print(NameRules().name_rules())