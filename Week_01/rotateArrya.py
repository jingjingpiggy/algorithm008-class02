#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>

# 时间复杂度O(k), 运行了152ms
# 暴力求解法
def rotate0(nums, k):
    while k >0:
        p = nums.pop(-1)
        nums.insert(0, p)
        k -= 1

# 切片
def rotate1(nums, k):
    nums[:] = nums[-k%len(nums):] + nums[:-k%len(nums)]



# 旋转三次
def rotate2(nums, k):
    k %= len(nums)

    def reverse(nums, start, end):
        while start <  end:
            nums[start] ^= nums[end]
            nums[end] ^= nums[start]
            nums[start] ^= nums[end]
            start += 1
            end -= 1

    reverse(nums, 0, len(nums)-1)
    print(nums)
    reverse(nums, 0, k-1)
    print(nums)
    reverse(nums, k, len(nums) -1)

    return nums

def rotate3(nums, k):
    k %= len(nums)

    def reverse(nums, start, end):
        while start <  end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1

    reverse(nums, 0, len(nums)-1)
    print(nums)
    reverse(nums, 0, k-1)
    print(nums)
    reverse(nums, k, len(nums) -1)

    return numsprint(rotate2([1,2,3,4,5,6,7], 3))
