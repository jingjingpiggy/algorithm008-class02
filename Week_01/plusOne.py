#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
def plusOne1(digits):
    # 加法器
    p = 1
    for i in range(len(digits), 0, -1):
        r = digits[i-1] + p
        if r >= 10:
            p = 1
            digits[i-1] = 0
        else:
            p = 0
            digits[i-1] = r
    if p == 1:
        digits = [1] + digits
    return digits

def plusOne2(digits):
    for i in range(len(digits)-1, -1, -1):
        if digits[i] != 9:
            digits[i] = digits[i] + 1
            return digits
        digits[i] =  0
    return [1] + digits

def plusOne3(digits):
    sums = 0
    for i in digits:
        sums = sums*10 +i
    sums_str = str(sums + 1)
    return list(map(int, list(sums_str)))

def plusOne4(digits):
    s = [str(x) for x in digits]
    res = int(''.join(s)) + 1

    i = [int(x) for x in str(res)]
    return i

def plusOne5(digits):
    i = int("".join(map(str, digits))) + 1
    res = list(map(int, str(i)))
    return res

print(plusOne3([1,2,9]))
