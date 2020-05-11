#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
def subset(nums):
    #import ipdb;ipdb.set_trace()
    #res = [[]]
    #for i in nums:
    #    for num in nums:
    #        res = res + [[i] + [num]]
    #return res
    res = [[]]
    for num in nums:
        new = []
        for subset in res:
            new_subset = subset + [num]
            new.append(new_subset)

        res.extend(new)
    return res


print(subset([1,2,3]))
