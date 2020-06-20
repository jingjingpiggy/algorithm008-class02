#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
def isMatch(s, p):
    s = '0'+s
    p = '0'+p
    dp = [[False for _ in range(len(p))] for _ in range(len(s))]

    dp[0][0] = True
    for i in range(1, len(p)):
        dp[0][i] = dp[0][i-1] and p[i] == '*'
    for i in range(1, len(s)):
        dp[i][0] = False

    for i in range(1, len(s)):
        for j in range(1, len(p)):
            if s[i] == p[j] or p[j] == '?':
                dp[i][j] = dp[i-1][j-1]
            elif p[j] == '*':
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
    return dp[-1][-1]
