#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
def nthUglyNumber(n):
    dp = [1 for _ in range(n)]
    # 三指针初始化
    i2 = 0
    i3 = 0
    i5 = 0
    for i in range(1,n):
        min_val = min(dp[i2]*2,dp[i3]*3,dp[i5]*5)
        dp[i] = min_val
        # 找出哪个指针对应的数造出了现在这个最小值，将指针前移一位
        if dp[i2]*2 == min_val:
            i2 += 1
        if dp[i3]*3 == min_val:
            i3 += 1
        if dp[i5]*5 == min_val:
            i5 += 1
    return dp[-1]


def nthUglyNumber2(n):
    dp, a, b, c = [1] *n, 0, 0, 0
    for i in range(1, n):
        n2, n3, n5 = dp[a]*2, dp[b]*3, dp[c]*5
        dp[i] = min(n2, n3, n5)
        if dp[i] == n2: a += 1
        if dp[i] == n3: b += 1
        if dp[i] == n5: c += 1
    return dp[-1]

print(nthUglyNumber2(10))
