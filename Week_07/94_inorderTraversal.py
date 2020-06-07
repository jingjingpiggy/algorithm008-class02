#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
def inorderTraversal(root):
    res = []
    def dfs(root):
            if not root:
                    return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
    dfs(root)
    return res
