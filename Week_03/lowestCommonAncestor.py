#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
def lowestCommonAncestor(root, p, q):
    # 如果左子树为空，则返回右子树；如果右子树为空，则返回左子树
    # 如果分别在左右，子树中则返回根节点
    # 如果每层都没找到就会从下往上返回空，空，空。。。
    if not root or root==p or root ==q:
        return root
    l = lowestCommonAncestor(root.left, p, q)
    r = lowestCommonAncestor(root.right, p, q)
    if not l: return r
    if not r: return l
    return root
