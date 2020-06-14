#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
def merge(nums1, m, nums2, n):
    i, j = 0, 0
    while j < n:
        if i >= m+j:
            nums1[i:i+n-j] = nums2[j:n]
            break
        if nums1[i] < nums2[j]:
            i += 1
        else:
            nums1[i], nums1[i+1:] = nums2[j], nums1[i:len(nums1)-1]
            j += 1
            i += 1
    return nums1

print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))
