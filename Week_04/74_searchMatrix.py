#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    m = len(matrix)
    if m == 0: return False
    n = len(matrix[0])

    left, right = 0, m*n-1

    while left <= right:
        pivot = (left + right)//2
        i = pivot // n
        j = pivot % n
        pivot_ele = matrix[i][j]
        if pivot_ele == target: return True
        elif pivot_ele > target:
            right = pivot - 1
        else:
            left = pivot + 1
    return False

print(searchMatrix([[1,3,5,7],[10,11,16,30],[23,30,34,50]], 3))
