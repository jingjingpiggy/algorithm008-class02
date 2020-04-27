#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
def minimumAbsDifference(arr):
    arr = sorted(arr)
    ans = []
    pair_list = []
    diff = abs(arr[1] - arr[0])

    for i in range(len(arr) -1):
        if abs(arr[i+1] - arr[i]) <= diff:
            pair_list.append([arr[i], arr[i+1]])
            diff = abs(arr[i+1] - arr[i])

    for i in range(len(pair_list)):
        if abs(pair_list[i][1] - pair_list[i][0]) == diff:
            ans.append(pair_list[i])

    return ans

print(minimumAbsDifference([4,2,1,3]))

def minimumAbsDifference2(A):
    L, D, m, _ = len(A), [], float('inf'), A.sort()
    for i in range(L-1):
        d = A[i+1] - A[i]
        if d == m: D.append([A[i],A[i+1]])
        elif d < m: D, m = [[A[i],A[i+1]]], d
    return D


def minimumAbsDifference3(A):
    L, D, _ = len(A), collections.defaultdict(list), A.sort()
    for i in range(L-1): D[A[i+1] - A[i]].append([A[i],A[i+1]])
    return D[min(D.keys())]
