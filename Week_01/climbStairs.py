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
    if n <=2:
        return n
    for i in range(1, n+1) {
        n[i] = n[i-1] + n[i-2]
    }

def climbStairs(n):
    if n <= 2:
        return n
    f1, f2, f3 = 1, 2, 3
    for i in range(3, n+1):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
    return f3
