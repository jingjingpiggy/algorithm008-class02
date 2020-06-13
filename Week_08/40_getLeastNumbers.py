#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
# 布隆过滤器
def getLeastNumbers(arr, k):
    nums = [0] * 10000
    for a in arr:
        nums[a] += 1
    output = []
    i = 0
    while len(output) < k:
        if nums[i] >= 1:
            for j in range(nums[i]):
                output.append(i)
        i += 1
    return output[:k]

print(getLeastNumbers([3,2,1], 2))
