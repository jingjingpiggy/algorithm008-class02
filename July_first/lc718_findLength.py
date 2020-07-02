#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
class Solution:
    def findLength(self, A, B):
        m = len(A)
        n = len(B)
        ans = 0
        # 此处在多了一行一列，为了给dp做周转
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
       # import ipdb;ipdb.set_trace()
        for i in range(1, m+1):
            for j in range(1, n+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        print(dp)
        return ans

    def findLength2(self, A, B):
        m, n = len(A)+1, len(B)+1
        dp=[[0] * n for _ in range(m)]

        ans = 0
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j-1] + 1 if A[i-1] == B[j-1] else max(dp[i-1][j], dp[i][j-1])
                ans = max(ans, dp[i][j])
        return ans
c = Solution()
print(c.findLength2([3,2,1,4,7],[1,2,3,2,1]))
