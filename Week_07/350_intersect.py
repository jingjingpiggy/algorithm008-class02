#!/usr/bin/env python
#-*- coding:utf-8 -*-
import collections
# Author: Li jinjing <lijinjing@gmail.com>
# https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/solution/jin-jie-san-wen-by-user5707f/
def intersect(nums1, nums2):
    nums1.sort()
    nums2.sort()
    r = []
    left, right = 0, 0
    while left < len(nums1) and right < len(nums2):
        if nums[left] < nums2[right]:
            left += 1
        elif nums1[left] == nums2[right]:
            r.append(nums1[left])
            left += 1
            right += 1
        else:
            right += 1
    return r

def intersec2(nums1, nums2):
    n1, n2 = collections.Counter(nums1), collections.Counter(nums2)
    res = []
    for i in n1:
        tmp=min(n1[i], n2[i])
        while tmp > 0:
            res.append(i)
            tmp -= 1
    return res
