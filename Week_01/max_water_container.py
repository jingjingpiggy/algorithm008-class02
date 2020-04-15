#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>

# 复杂度为O(n^2),当参数很多的时候时间会很久
def maxArea(height):
    m = 0
    for i in range(0, len(height)-1):
        for j in range(i+1, len(height)):
            area = (j-i) * min(height[i], height[j])
            m = max(area, m)
    return m

print(maxArea([1,8,6,2,5,4,8,3,7]))
