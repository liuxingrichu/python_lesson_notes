#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
该实例演示数字猜谜游戏
"""

number = 7
guess = -1

print("数字猜谜游戏!".center(36, '-'))
while guess != number:
    try:
        guess = input("请输入你猜的数字：")
        # print(type(guess))
        guess = int(guess)
    except ValueError as e:
        print("\033[0;31m\t请输入数字\033[0m")
        continue
    # print(type(guess))
    if guess == number:
        print("\033[0;32m\t恭喜，你猜对了！\033[0m")
    elif guess < number:
        print("\033[0;31m\t猜的数字小了...\033[0m")
    else:
        print("\033[0;31m\t猜的数字大了...\033[0m")
