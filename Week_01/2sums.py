#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
def twoSum(nums, target):
    if len(nums) < 2:
        return None
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            nums[i] = target - nums[j]
            return [nums[i], nums[j]]

print(twoSum([2,7,11,15], 9))
