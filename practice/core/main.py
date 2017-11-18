#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    列表练习题
"""


def reverse3(nums):
    """
    反转
    :param nums: 列表
    :return:反转后的列表
    """
    nums.reverse()
    return nums


def make_ends(nums):
    """
    收尾组合新列表
    :param nums: 列表
    :return:收尾组合的新列表
    """
    return [nums[0], nums[-1]]


def sum13(nums):
    """
    数组中13，及之后的一个元素，不计算在总和之中
    :param nums: 列表
    :return:除列表中13及之后的一个元素外的，全部计算之和
    """
    new_nums = list()
    flag = False
    for i in range(len(nums)):
        if flag:
            flag = False
            continue
        if nums[i] is not 13:
            new_nums.append(nums[i])
        else:
            if i + 1 is not len(nums):
                flag = True
            else:
                break
    return sum(new_nums)


def has22(nums):
    """
    判定列表中是否有连续两个2
    :param nums: 列表
    :return:存在两个连续的2，返回True，否则，返回False
    """
    while nums.count(2) > 1:
        position = nums.index(2)
        if nums[position + 1] is 2:
            return True
        else:
            del nums[position]
    else:
        return False
