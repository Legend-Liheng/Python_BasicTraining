# -*- encoding: utf-8 -*-
"""
@File    : 56-json文件的读取.py
@Time    : 2020/8/29 15:29
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

import json

with open('../test.json', 'r', encoding='UTF-8') as my_json:

    value = json.load(my_json)
    print(value)

    print(value['no'])
    print(value['name'])
    print(value['age'])

    # v = json.loads(value['no'])

