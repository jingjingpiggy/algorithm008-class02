#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
def combine(n, k):
    res = []
    def dfs(nums, k, index, path):
    #if k < 0:  #backtracking
        #return
        if k == 0:
            res.append(path)
            return # backtracking
        for i in range(index, len(nums)):
            dfs(nums, k-1, i+1, path+[nums[i]])

    import ipdb;ipdb.set_trace()
    dfs(range(1,n+1), k, 0, [])
    return res


print(combine(4, 2))
