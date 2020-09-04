# -*- encoding: utf-8 -*-
"""
@File    : 53-Excel文件的写入.py
@Time    : 2020/8/28 14:46
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

import xlsxwriter, xlrd

# 打开excel文件
# workexcel = xlsxwriter.Workbook('student.xlsx')

with xlsxwriter.Workbook('../test.xlsx') as workexcel:

    # 给文件创建一张工作表
    worksheet = workexcel.add_worksheet('工作表1')

    # 给工作表设置第一行信息
    worksheet.write(0, 0, '学号')
    worksheet.write(0, 1, '姓名')
    worksheet.write(0, 2, '年龄')

    # 定义一个字典，记录学生信息
    student_info = [{'no': 'XM001', 'name': '李恒1', 'age': '28'},
                    {'no': 'XM002', 'name': '欧阳春', 'age': '18'},
                    {'no': 'XM003', 'name': '李逍遥', 'age': '19'}]

    # 给工作表插入学生信息
    for i, value in enumerate(student_info):
        worksheet.write(i + 1, 0, value['no'])
        worksheet.write(i + 1, 1, value['name'])
        worksheet.write(i + 1, 2, value['age'])
        # print(i, value['no'])
        # print(i, value['name'])
        # print(i, value['age'])

# workexcel.close()