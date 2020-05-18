#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
def findContentChildren(g,s):
    # child
    g.sort()
    # cookie
    s.sort()
    child = cookie = 0

    while child < len(g) and cookie < len(s):
        # 能够满足一个孩子的胃口
        if g[child] <= s[cookie]:
            # 孩子饱了
            child+=1
        # 饼干吃了
        cookie += 1
    # 返回被满足的孩子数
    return child
