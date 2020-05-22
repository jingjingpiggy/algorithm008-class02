#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
def solveNQueens(n):
    def DFS(queens, xy_dif, xy_sum):
        # queens: 一维数组，存着每一行皇后的位置，也就是列
        # x-y
        # x+y
        p = len(queens)
        if p==n:
            result.append(queens)
            return None
        for col in range(n):
            if col not in queens and p-col not in xy_dif and p+col not in xy_sum:
                DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])

    result = []
    DFS([],[],[])

    return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]


print(solveNQueens(4))
