#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
# 暴力：n^2
# DP: a.分治(子问题): problem(i) = sub(i-1)
#     b.状态数组定义
#     c.DP方程

def maxSubArray(nums):
    #dp问题，公式：dp[i] = max(nums[i], nums[i] + dp[i-1])
    #最大子序和 = 当前元素自身最大，或者 包含之前后 最大
    import ipdb;ipdb.set_trace()
    for i in range(1, len(nums)):
        nums[i] = max(nums[i], nums[i] + nums[i-1])

    return max(nums)

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
