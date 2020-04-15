#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
# 斐波那契数列
# 1: 1
# 2: 2
# 3: f(1) + f(2)
# 4: f(2) + f(3)
# f(3) = f(1) + f(2)
# f(4) = f(2) + f(3)
# ....

def Fibonacci(n):
    if n == 0: return 0
    if 1 <= n <= 2: return 1

    f1 = 0
    f2 = 1

    for i in range(2, n+1):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
    return f3


def climbStairs(n):
    if n <= 2:
        return n
    f1, f2, f3 = 1, 2, 3
    for i in range(3, n+1):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
    return f3
