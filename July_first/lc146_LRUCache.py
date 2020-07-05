#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity):
        self.remain = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache: return -1
        val = self.cache.pop(key)
        self.cache[key] = val
        return val

    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        else:
            if self.remain >0 : self.remain -= 1
            else:
                self.cache.popitem(last=False) #cache工作站的底部，也就是最久没有被使用的那个
        self.cache[key] = value
