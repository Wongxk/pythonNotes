#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
# 策略模式：完成一件事情有多种实现方法（多种算法）时，可以考虑使用策略模式。比如，你去上学，可以选择骑自行车，坐公交，
          坐地铁，开车或者走路，这只取决于你一时的条件跟决定。
# 需求：做一个商场收银软件，营业员根据客户所购买商品的单价和数量，向客户收费。商场会有正常收费，打折，满减等不同收费策略。

# 第一步：编写一个方法完成统计客户总价。
# 第二步：增加打折算法。
# 第三步：用简单工厂模式实现收费的新策略：正常收费，打折收费，满减收费。
# 第四步：http://www.imooc.com/wiki/detail/id/137 学习策略模式结构，使用策略模式改善代码。
# 第五步：将策略模式与工厂模式结合完成需求。
'''

total_price = 0.0


def get_total_price():
    return total_price


def add_goods(price, count):
    total_p = get_total_price()
    total_p += price * count
    return total_p
