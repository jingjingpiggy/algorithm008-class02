#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
# 暴力解法
def twoSum(nums, target):
    if len(nums) < 2:
        return None
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            nums[i] = target - nums[j]
            return [nums[i], nums[j]]


def twoSum1(nums, target):
    if len(nums) < 2:
        return None

    d = {i: x for x, i in enumerate(nums)}
    for i in range(len(nums)):
        data = nums[i]
        if target - data in d:
            return [d[target-data], i]

print(twoSum1([2,7,11,15], 9))
