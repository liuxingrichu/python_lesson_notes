#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 方法一
sum = 0
for num in range(1, 101):
    if num % 2:
        sum += num
        # print(num)

print("1-100数字之间的奇数之和是", sum)

# 方法二
sum = 0
for num in range(1, 101, 2):
    sum += num

print("1-100数字之间的奇数之和是", sum)