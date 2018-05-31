#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random
a=random.randint(1,100)
print(a)
print("---开始猜数字游戏---")
b=int(input("请输入你的数字:"))
while a!=b:
    if(b>a):
        print("\033[0;31m你猜大了\033[0m")
        b = int(input("\033[0;31m请输入你的数字:\033[0m"))
    elif b<a:
        print("\033[0;31m你猜小了\033[0m")
        b = int(input("\033[0;31m请输入你的数字:\033[0m"))
else:
    print("\033[0;33m恭喜你猜对了\033[0m")