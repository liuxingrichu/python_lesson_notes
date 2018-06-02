#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
	购物车

	需求分析
	    1. 启动程序后，输入用户名密码后，让用户输入购物卡金额，然后打印商品列表
	    2. 允许用户根据商品编号购买商品
	    3. 用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
	    4. 可随时退出，退出时，打印已购买商品和余额
	    5. 在用户使用过程中， 关键输出，如余额，商品已加入购物车等消息，需高亮显示

	知识储备

	编程思路
        1. 用变量存储用户名和密码
        2. 用元组存储存储商品信息（名称、单价）
        3. 用列表存储用户购物信息
        4. 用条件语句和循环语句，判定用户是否合法；
            若用户非法，提示并进入用户信息输入模式
            若用户合法，提示欢迎信息，并用变量接收用户购物卡金额信息
        5. 用字符串、列表、元组方法输出商品清单
        6. 接收用户输入操作，若接收内容非商品可选清单和退出信息情况下，友情提示，
            并再次打印商品信息
        7. 若接收的是商品序列号，检测余额是否够，够就直接扣款，并添加到用户购物车中，
            不够就提醒用户
        8. 若接收的是用户退出信息，首先打印用户购物清单，再打印用户购物卡余额，
            最后，友情提示，并退出系统

	编程实现与调试

"""

username = '1'
password = '1'
goods = (('python', 99), ('iphone', 8000), ('bike', 600), ('coffee', 38),
         ('fly', 500))
goods_chart = []
money = None
flag = True

while flag:
    while True:
        user = input("用户名: ").strip()
        passwd = input("密  码: ").strip()
        if user is username and passwd is password:
            print("\t\033[32;0m欢迎%s登陆购物天堂\033[0m" % username)
            break
        else:
            print("\t\033[31;0m用户名或密码有误！\033[0m")

    print("商品清单".center(26, '-'))
    for i, good in enumerate(goods):
        print("\t%s\t%s\t%s" % (i + 1, good[0], good[1]))
    print("end".center(30, '-'))
    while True:
        money = input("充值金额: ").strip()
        if not money:
            continue
        if money.isdigit():
            money = int(money)
            break
        else:
            print('\t\033[31;0m请输入数字！')

    while True:
        num = input("选择商品序号或退出('q'): ").strip()
        if not num:
            continue

        if num is 'q':
            if not goods_chart:
                print("\t\033[36;0m您好，%s, 本次您未购买任何商品！\033[0m" % user)
            else:
                print("\t\033[32;0m尊敬的顾客%s，您的购物信息和购物卡余额如下：\033[0m" % user)
                print("购物清单".center(26, '-'))
                for i, good in enumerate(goods_chart):
                    print("\t%s\t%s\t%s" % (i + 1, good[0], good[1]))
                print("end".center(30, '-'))
            print('\t余额: \033[31;0m%s\033[0m' % money)
            print("\t\033[32;0m尊敬的顾客%s，欢迎您的下次光顾！\033[0m" % user)
            flag = False
            break
        elif num.isdigit():
            num = int(num)
            if num > 0 and num <= len(goods):
                name = goods[int(num) - 1][0]
                price = goods[int(num) - 1][1]
                if money >= price:
                    money -= price
                    goods_chart.append((name, price))
                    print('\t\033[32;0m商品%s已成功添加到购物车！\033[0m' % name)
                else:
                    print('\t\033[31;0m余额不足，请充值！\033[0m')
            else:
                print("\t\033[31;0m输入有误，请输入有效商品序号！\033[0m")
        else:
            print("\t\033[31;0m输入有误，请输入商品序号或退出\033[0m")
