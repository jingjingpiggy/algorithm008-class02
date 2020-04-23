#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
def addDigits(num):
    # Recursive
    if num < 10:
        return num

    s = 0
    for i in list(str(num)):
        s += int(i)
    return addDigits(s)

print(addDigits(38))

def addDigits2(num):
    while num >= 10:
        sum = 0
        while num > 0:
            sum += num % 10
            num //= 10
        num = sum
    return num

def addDigits3(num):
    return (num-1)%9 + 1 if num!=0 else 0
