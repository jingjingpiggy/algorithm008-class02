#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
def setZeroes(matrix):
    row = len(matrix)
    lie = len(matrix[0])

    l =[]
    for i in range(len(matrix)):
        for j in matrix[i]:
            if j == 0:
                l.append([i, matrix[i].index(j)])
    print(l)

    #import ipdb;ipdb.set_trace()

    for each in l:
        for x in range(row):
            for y in range(lie):
                if x == each[0]:
                    matrix[x][y] = 0
                if y == each[1]:
                    matrix[x][y] = 0
    return matrix
print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
