#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
def myPow(x, n):
    # 暴力
    result = 1
    for i in range(0, n):
        result *= x
    return result


def myPow2(x, n):
    # 分治
    def quickMul(n):
        if n == 0:
            return 1.0
        y = quickMul(n//2)
        return y*y if n % 2 == 0 else y*y*x

    return quickMul(n) if n >=0 else 1.0/quickMul(-n)

print(myPow2(2, 2))
