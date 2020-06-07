#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
def findCircleNum(M):
    """
    :type M: List[List[int]]
    :rtype: int
    """
    father = [i for i in range(len(M))]

    def find(a):
        if father[a] != a: father[a] = find(father[a])
        return father[a]

    def union(a, b):
        father[find(b)] = find(a)
        return find(b)

    for a in range(len(M)):
        for b in range(a):
            if M[a][b]: union(a, b)
    for i in range(len(M)): find(i)
    return len(set(father))
