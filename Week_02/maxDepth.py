#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
def maxDepth(root):
# DFS
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

def maxDepth2(root):
    # list BFS

    if not root:
        return 0

    stack = [root]
    i = 0
    while len(stack) != 0:
        n = len(stack)
        i += 1
        for k in range(n):
            temp = stack.pop(0)
            if temp.left:
                stack.append(temp.left)
            if temp.right:
                stack.append(temp.right)
    return i

from collections import deque
def maxDepth3(root):
# deque BFS
    if not root:
        return 0

    queue = deque()
    queue.append(root)

    lenth = 0

    while queue:
        lenth += 1
        for i in range(len(queue)):
            node = queue.popleft()
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
    return lenth

print(maxDepth3([3,9,20,null,null,15,7]))
