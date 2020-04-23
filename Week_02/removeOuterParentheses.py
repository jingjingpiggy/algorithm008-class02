#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
def removeOuterParentheses(s):
    import ipdb;ipdb.set_trace()
    stack = []
    result = ''
    for i in s:
        if i == '(':
            stack.append(i)
            if len(stack) > 1:
                result += '('
        else:
            stack.pop()
            if len(stack) != 0:
                result += ')'

    return result

def removeOuterParentheses2(s):
    l, res = 0, ""
    for c in s:
        if c == "(":
            if l > 0:
                res += c
            l += 1
            print(l)
        else:
            if l > 1:
                res += c
            l -=1
    return res
print(removeOuterParentheses2("(()())(())"))
