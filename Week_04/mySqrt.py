#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
def mySqrt(x):
    # 二分查找
    low, high, res = 0, x, 0

    while low <= high:
        mid = (low + high)//2
        guess = mid * mid
        if guess == x:
            return mid
        elif guess > x:
            high = mid -1
        else :
            res = mid
            low = mid + 1

    return res


def mySqrt2(x):
    import ipdb;ipdb.set_trace()
    r = x
    while r * r >x:
        r  = (r + x/r)/2
    return r

print(mySqrt2(8))
