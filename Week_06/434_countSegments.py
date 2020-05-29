#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
def countSegments(s):
    #1
    if not s.strip(" "): return 0
    return len(s.split())

    #2
    l = len(s)
    nw = 0
    for i in range(0, l):
        if (i==0 and s[i]!=" ") or (s[i]!=" " and s[i-1]==" "):
            nw += 1
    return nw
