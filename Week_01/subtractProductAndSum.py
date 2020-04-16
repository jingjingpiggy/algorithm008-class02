#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
# leetcode 1281
def subtractProductAndSum(n):
    p = 1
    s = 0
    while n > 0:
        p *= n%10
        s += n%10
        n //=10
    return p-s
