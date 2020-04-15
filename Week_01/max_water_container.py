#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>

# leetcode11
# 复杂度为O(n^2),当参数很多的时候时间会很久
def maxArea0(height):
    m = 0
    for i in range(0, len(height)-1):
        for j in range(i+1, len(height)):
            area = (j-i) * min(height[i], height[j])
            m = max(area, m)
    return m

#夹逼的办法
def maxArea1(height):
    m = 0
    i = 0
    j = len(height) - 1

    while i<j:
        if height[i] < height[j]:
            minHeight = height[i]
            i += 1
        else:
            minHeight = height[j]
            j -= 1
        area = (j-i+1) * minHeight
        m = max(m, area)
    return m

print(maxArea1([1,8,6,2,5,4,8,3,7]))
