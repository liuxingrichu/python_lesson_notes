#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 编程输出斐波那契数列的前10项
a = 0
b = 1
c = 1
num = 0

while num < 10:
    print(c, end=' ')
    c = a + b
    num += 1
    a, b = b, c
print()

# 编程输出在100以内的斐波那契数列
a = 0
b = 1
c = 1

while c < 100:
    print(c, end=' ')
    c = a + b
    a, b = b, c
print()

