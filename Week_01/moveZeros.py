#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>

def moveZeros(nums):
#    zero = 0
#    for i in range(len(nums)):
#        if nums[i] != 0:
#            nums[i], nums[zero] = nums[zero], nums[i]
#            zero += 1
#    print(nums)

    #j = 0
    #for i in range(len(nums)):
    #    if nums[i] != 0:
    #        nums[i], nums[j] = nums[j], nums[i]
    #        j += 1
    #print(nums)

    for i in nums:
        if i == 0:
            nums.append(0)
            nums.remove(0) # 在循环中 删除第一个为0的地方，其他的元素都往前挪动一位。最坏时间复杂度O(n^2), 时间复杂度很高

moveZeros([0,1,0,12,13])
