#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
def sortColors(nums):
    i = cur = 0
    j = len(nums) - 1

    while cur <= j:
        if nums[cur] == 0:
            if cur != i:
                nums[cur], nums[i] = nums[i], nums[cur]
            cur += 1
            i += 1
        elif nums[cur] == 2:
            nums[cur], nums[j] = nums[j], nums[cur]
            j -= 1
        else:
            cur += 1


def sortColors2(nums):
    cnt = [0] * 3
    for n in nums: cnt[n] += 1
    i = 0
    for cur in range(3):
        for j in range(cnt[cur]):
            nums[i] = cur
            i += 1
