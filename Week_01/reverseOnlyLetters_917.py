#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>

def reverseOnlyLetters(s):
    # 双指针
    i, j = 0, len(s)-1
    s = list(s)

    while i <= j:
        if not s[i].isalpha():
            i += 1
        elif not s[j].isalpha():
            j -= 1
        else:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

    return "".join(s)

print(reverseOnlyLetters("Test1ng-Leet=code-Q!"))
