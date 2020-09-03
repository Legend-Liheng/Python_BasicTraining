# -*- encoding: utf-8 -*-
"""
@File    : 55-json文件的写入.py
@Time    : 2020/8/29 15:29
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

import json

# myjson = open('test.json', 'w', 'UTF-8')
#
# myjson.write('no')

student_info = {'no': 'XM001', 'name': '李2', 'age': '30'}
# print(type(student_info))
print(student_info)

# 将字典数据转化成json数据，ensure_ascii= False时，可输入中文
json_str = json.dumps(student_info, ensure_ascii= False)

print(type(json_str))
# print(json_str)
#
# print(type(json.loads(json_str)))
# print(json.loads(json_str))

with open('test.json', 'w', encoding= 'UTF-8') as f:
    f.write(json_str)

# with open('test.json', 'w', encoding= 'UTF-8') as f:
#     f.write(json.dump(student_info, fp= 0))


