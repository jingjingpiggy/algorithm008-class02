#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>

def isAnagram(s, t):
    # 242 1. 暴力, sort, sorted_str 相等? ONlogN
    s.sort()
    s.sort()
    return s == t
    # hash, map --> 统计每个字符的频次


return isAnagram()
