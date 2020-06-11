#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
def relativeSortArray(arr1, arr2):
    dic = {}
    for elem in arr1:
        if not dic.get(elem):
            dic[elem]=1
        else:
            dic[elem] = dic[elem] + 1

    output = []
    #import ipdb;ipdb.set_trace()
    for elem in arr2:
        output += [elem] * dic[elem]

    extra_output = []
    for elem in set(arr1) - set(arr2):
        extra_output += [elem] * dic[elem]

    return output + sorted(extra_output)


import collections
def relativeSortArray2(arr1, arr2):
    c = collections.Counter(arr1)
    res = []
    for i in arr2:
        res += [i] * c.pop(i)
    return res+sorted(c.elements())

print(relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))
