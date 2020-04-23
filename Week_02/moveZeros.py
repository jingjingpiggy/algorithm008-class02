#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
def moveZeroes(nums):
    zero = 0
    for i in range(len(nums)):
        if nums(i) != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1
    return nums
