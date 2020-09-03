# -*- encoding: utf-8 -*-
"""
@File    : 51-txt文件的写入.py
@Time    : 2020/8/28 14:40
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

# # 以只写模式打开文件，若没有则先创建
# f = open('test.txt', 'w', encoding= 'UTF-8')
#
# # 写入数据
# f.write('李恒')
#
# # 操作完成后，关闭文件
# f.close()

# 这种写法等价于上面的代码，省略了close操作
with open('test.txt', 'w', encoding= 'UTF-8') as f:
    f.write('哈哈')