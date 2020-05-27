#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>

def fib(n):
    if n <= 1: return n
    else:
        return fib(n-1) + fib(n-2)


# 自顶向下:递归+记忆化搜索
def fib2(n):
    memo = [0]*(n+1)
    if n <= 1: return n
    # memo数组来进行记忆化搜索，斐波那契树上的子状态都从memo中取即可，如果计算过了就不再重复计算,计算过的memo[n]就不会等于0, 时间复杂度为线性的On
    if memo[n] == 0:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

print(fib2(5))


# 自底向上
def fib3(n):
    if n == 0: return 0
    if 1 <= n <=2: return 1

    f1, f2 = 0, 1
    for i in range(2, n+1):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
    return f3
