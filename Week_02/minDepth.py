#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
def minDepth(root):
# BFS
    if not root: return 0
    queue = [(1, root)]
    while queue:
        depth, node = queue.pop(0)
        if not node.left and not node.right:
            return depth
        if node.left:
            queue.append((depth+1, node.left))
        if node.right:
            queue.append((depth+1, node.right))


def minDepth(root):
#DFS
    if not root: return 0
    stack = [(1, root)]
    min_depth=float('inf')
    while stack:
        depth, node = stack.pop(0)
        if not node.left and not node.right:
            min_depth = min(min_depth, depth)
        if node.left:
            stack.append((depth+1, node.left))
        if node.right:
            stack.append((depth+1, node.right))
    return min_depth
