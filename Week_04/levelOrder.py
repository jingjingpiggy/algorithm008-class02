#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
from collections import deque

def levelOrder(root):
    if not root: return []
    queue, res = deque([root]), []

    while queue:
        cur_level, l = [], len(queue)
        for i in range(0, l):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            cur_level.append(node.val)
        res.append(cur_level)
    return res

def levelOrder2(root):
    nodes = [(root,)]
    values = []

    while nodes:
        values.append([r.val for i in nodes for j in i if j])
        nodes = [r.left, r.right for i in nodes for j in i if j]
    return values[:-1]
