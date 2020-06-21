#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
def reverseStr(s , k):
    result=''
    for i in range(0,len(s),2*k):
        tmp=s[i:i+k]
        tmp=tmp[::-1]+s[i+k:i+2*k]
        re+=tmp
    return result
