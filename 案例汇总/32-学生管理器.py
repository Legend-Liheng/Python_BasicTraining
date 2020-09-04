# -*- encoding: utf-8 -*-
"""
@File    : 32-名片管理器.py
@Time    : 2020/8/9 10:31
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""
# 定义两个变量用来保存具体学生信息以及全部学生信息
all_dict = {}
student_dict = {}

for i in range(50):
    chose = int(input('''-----欢迎使用学生管理系统------
1.添加学生
2.删除学生
3.修改学生
4.查询学生
5.退出系统
请输入你的选择：'''))

    if chose == 1:
        name = input("请输入学生姓名：")
        age = int(input("请输入学生年龄："))

        student_dict = {"name": name, "age": age}
        all_dict[name] = student_dict
        print("添加成功！")

    elif chose == 2:
        chose_student = input("请输入要删除的学生姓名：")

        if chose_student in all_dict.keys():
            del all_dict[chose_student]
            print("删除后的学生列表：", all_dict)
        else:
            print("查无此人！")

    elif chose == 3:
        chose_student = input("请输入要修改的学生姓名：")

        if chose_student in all_dict.keys():
            name = input("请输入修改后的姓名：")
            all_dict[chose_student]['name'] = name
            print("修改后的学生信息：", all_dict[chose_student])
        else:
            print("查无此人！")

    elif chose == 4:
        print("1.查全部学生")
        print('2.查特定学生')
        chose_type = int(input("请输入你的选择："))
        if chose_type == 1:
            print(all_dict)
        elif chose_type == 2:
            chose_student = input("请输入想查询的学生姓名：")

            if chose_student in all_dict.keys():
                print(all_dict[chose_student])
            else:
                print("查无此人！")
        else:
            print("输入有误！！！")

    elif chose == 5:
        print("欢迎下次使用程序！！")
        break
    else:
        print("输入有误！！！")


