#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
# 状态表示: dp[i]: 到第i个台阶的走法数量
# 状态转移: dp[i] = dp[i-1] + dp[i-2]  i>=2
# 边界情况：dp[0] = 1, dp[1] = 1

if n<=1: retturn 1

prev, curr = 1, 1
for i in range(2, n+1):
    next = prev+curr
    prev = curr
    curr = next
return curr
