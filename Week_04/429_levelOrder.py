#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
class TreeNode(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

Tree1 = TreeNode(1)
Tree3 = TreeNode(3)
Tree2 = TreeNode(2)
Tree4 = TreeNode(4)
Tree5 = TreeNode(5)
Tree6 = TreeNode(6)

Tree1.val = 1
Tree1.children = [Tree3, Tree2, Tree4]
Tree2.val = 2
Tree2.children = None
Tree3.val = 3
Tree3.children = [Tree5, Tree6]
Tree4.val = 4
Tree4.children = None
Tree5.val = 5
Tree5.children = None
Tree6.val = 6
Tree6.children = None

# [] 要比deque快很多。。。
from collections import deque
def levelOrder(root):
    if not root: return []

    #queue = deque([root])
    queue = [root]
    result = []

#    import ipdb;ipdb.set_trace()
    while queue:
        cur, l = [], len(queue)
        for i in range(0, l):
            node = queue.pop(0)
            children = node.children
            if children:
                queue.extend(children)
#            if node.children:
#                for each in node.children:
#                    queue.append(each)
            cur.append(node.val)
        result.append(cur)

    return result

print(levelOrder(Tree1))
