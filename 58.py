# -*- encoding: utf-8 -*-
"""
@File    : 58.py
@Time    : 2020/8/29 19:41
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

# coding:utf-8
import xml.dom.minidom

# 新建xml文档对象
xml = xml.dom.minidom.Document()

# 写入xml文档的方法
def create_xml_test(filename):



    # 创建第一个节点，第一个节点就是根节点了
    root = xml.createElement('root')

    # 写入属性（xmlns:xsi是命名空间，同样还可以写入xsi:schemaLocation指定xsd文件）
    root.setAttribute('xmlns:xsi', "http://www.w3.org/2001/XMLSchema-instance")

    # 创建节点后，还需要添加到文档中才有效
    xml.appendChild(root)

    # 一般根节点是很少写文本内容，那么给根节点再创建一个子节点
    text_node = xml.createElement('element')
    text_node.setAttribute('id', 'id1')
    root.appendChild(text_node)

    # 给这个节点加入文本，文本也是一种节点
    text = xml.createTextNode('hello world')
    text_node.appendChild(text)

    # 一个节点加了文本之后，还可以继续追加其他东西
    tag = xml.createElement('tag')
    tag.setAttribute('data', 'tag data')
    text_node.appendChild(tag)

    # 写好之后，就需要保存文档了
    f = open(filename, 'w')
    f.write(xml.toprettyxml(encoding='utf-8'))
    f.close()


if __name__ == '__main__':
    # 在当前目录下，创建1.xml
    create_xml_test('100.xml')