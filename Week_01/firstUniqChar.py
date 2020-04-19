#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>

def firstUniqChar(s):
    d = {}
    for c in s:
        d [c] = not c in d
    print(d)
    for c in s:
        if d[c]: return c
    return ' '


#def firstUniqueChar2(s):
#    import collections
#    return [ k for k, v in collections.Counter(s).items() if v == 1]+[' '][0]

print(firstUniqueChar2("abaccdeff"))
