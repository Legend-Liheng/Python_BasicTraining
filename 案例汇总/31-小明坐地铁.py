# -*- encoding: utf-8 -*-
"""
@File    : 31-计算字符个数.py
@Time    : 2020/8/9 9:50
@Author  : 李逍遥.Legend
@Email   : 1320474295@qq.com
@Software: PyCharm
@Target  :
"""

'''
    -----------票价规则----------
    轨道交通价格调整为：
    6公里(含)内3元;
    6公里至12公里(含)4元;
    12公里至22公里(含)5元;
    22公里至32公里(含)6元;
    32公里以上部分，每增加1元可乘坐20公里。
'''
#获取公里数
km = int(input("请输入乘坐公里数："))
# print(km)

#定义一个初始化票价
vaule = 0

if km <= 0:
    print("输入的公里数有误！！！")
elif km <= 6:
    vaule = 3
    print("单程票价：", vaule)
elif km <= 12:
    vaule = 4
    print("单程票价：", vaule)
elif km <= 22:
    vaule = 5
    print("单程票价：", vaule)
elif km <=32:
    vaule = 6
    print("单程票价：", vaule)
elif km > 32:
    a = (km - 33) // 20 + 1#考虑到刚好满20公里的整数倍情况，一次在32处+1，保障刚好满20的整数倍的时候，收费正确
    vaule = 6 + a
    print("单程票价：", vaule)

'''
    -----------折扣规则----------
    使用市政交通一卡通刷卡乘坐轨道交通，
    每自然月内每张卡支出累计满100元以后的乘次，价格给予8折优惠;
    满150元以后的乘次，价格给予5折优惠;
    支出累计达到400元以后的乘次，不再享受打折优惠。
'''
"""
    假设每个月，小明都需要上20天班，每次上班需要来回1次，即每天需要乘坐2次同样路线的地铁
    最终得出这"20"天小明做地铁消费多少钱?(20天 40个来回)
"""
#定义一个变量，保存总金额
total_money = 0
for n in range(40):
    if total_money < 100:
        total_money += vaule
    elif total_money < 150:
        total_money += vaule * 0.8
    elif total_money < 400:
        total_money += vaule * 0.5
    else:
        total_money += vaule

print("一周坐四十次总共花费：%.2f元" % total_money)




