#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
# 时间复杂度On，空间复杂度O1
def majorityElement(nums):
    major = 0
    count = 0

    for n in nums:
        if count == 0:
            major = n
        if major == n:
            count += 1
        else:
            count -= 1
    return major


def majorityElement2(nums):
    d = {}
    for i in nums:
        d[i] = d[i] + 1 if i in d else 1

    c = len(nums)//2

    for k, v in d.items():
        if v > c:
            return k
print(majorityElement2([2,2,1,3,1,2,2]))
