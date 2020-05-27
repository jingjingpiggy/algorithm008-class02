#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>

#1. 暴力穷举:递归，n层: 每一层可以左或者右，O2^n
#2. DP: a. 重复性(分治) problem(i, j) = min(sub(i+1, j), sub(i+1, j+1)) + a[i, j]
#       b. 定义状态数组: f[i, j]
#       c. DP方程: f[i, j] = min(f[i+1, j], f[i+1, j+1]) + a[i, j]

#Bottom-up
def minimumTotal(triangle):
    if not triangle: return
    dp = triangle
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            dp[i][j] += min(dp[i+1][j], dp[i+1][j+1])
    print(triangle[0][0])
    return dp[0][0]


def minimumTotal2(triangle):
    f = [0] * (len(triangle) +1)
    for row in triangle[::-1]:
        for i in range(row):
            f[i] = row[i] + min(f[i], f[i+1])
    return f[0]

#bottom-up, On space
def minimumTotal3(triangle):
    if not triangle: return

    # 所有的结果都保存在了res中，也就是修改了最底层的这个数组内容
    res = triangle[-1]
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(trangle[i])):
            res[j] = min(res[j], res[j+1]) + trangle[i][j]
    return res[0]
