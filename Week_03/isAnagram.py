#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
def isAnagram(s, t):
    # 32ms 快
    # On

    d = {}
    for i in s:
        d[i] = d[i] + 1 if i in d else 1

    for i in t:
        d[i] = d[i]  - 1 if i in d else -1

    for i in d.values():
        if i != 0:
            return False
    return True


def isAnagram(s, t):
    # 52ms
    # Onlogn
    return True if sorted(s) == sorted(t) else False


print(isAnagram("a", "b"))
