#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
def sortedSquares(A):
    i = 0
    length = len(A)
    while i < length:
        A[i] = A[i] * A[i]
        i += 1
    A.sort()
    return A

def sortedSquares1(A):
    return sorted([i*i for i in A])

def sortedSquares2(A):
    i = 0
    z = j = len(A)-1

    res = [0] * len(A)

    while i <= j:
        if A[i]**2 < A[j]**2:
            res[z] = A[j]**2
            j -= 1
            z -=1
        else:
            res[z] = A[i]**2
            i += 1
            z -= 1
    return res


print(sortedSquares2([-4, -1, 0, 3, 10]))
