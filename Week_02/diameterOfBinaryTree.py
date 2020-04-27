#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
m = 0
def diameterOfBinaryTree(root):
    def depth(root):
        if not root:
            return 0
        l = depth(root.left)
        r = depth(root.right)
        m = max(m, l+r)
        return max(l, r) + 1

    depth(root)
    return m
