# -*- encoding: utf-8 -*-
"""
@File    : 54-Excel文件的读取.py
@Time    : 2020/8/28 15:46
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

import xlrd

# workexcel = xlrd.open_workbook('student.xlsx')
with xlrd.open_workbook('test.xlsx') as workexcel:

    # 通过工作表序号获取工作表数据
    # table = workexcel.sheet_by_index(0)
    # 通过工作表名称获取工作表数据
    table = workexcel.sheet_by_name('工作表1')

    # 获取行数
    rows = table.nrows
    # print('总行数：', rows)

    # 获取列数
    cols = table.ncols
    # print('总列数：', cols)

    # 获取工作表每一行的值（不建议）
    # value_rows = table.get_rows()
    # for i in valuerows:
    #     print(i)

    value_row_list = []

    # 通过行值获取对应行的值
    for n in range(0, rows):
        valuerows = table.row_values(n)

        if valuerows:
            value_row_list.append(valuerows)

    print(value_row_list)

    # 获取工作表每一列的值
    for m in range(0, cols):
        valuecols = table.col_values(m)
        print(valuecols)



