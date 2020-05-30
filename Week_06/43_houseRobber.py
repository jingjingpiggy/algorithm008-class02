#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
# 状态表示：dp[i] 表示从0到i偷到的最大总数
# 状态转移: dp[i] = Max(dp[i-2] + nums[i], dp[i-1]) //偷不偷当前的房子
# 边界情况：dp[0] = nums[0], dp[1]= Math.max(nums[0], nums[1])

if not nums or len(num) == 0:
    return 0

length = len(nums)
if length == 1: return nums[0]
if length == 2: return max(nums[0], nums[1])

prev = nums[0], curr = max(nums[0], nums[1])
for i in range(2, n):
    next = max(prev + nums[i], curr)
    prev = curr
    curr = next
return curr
