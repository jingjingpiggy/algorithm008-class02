#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

Tree15 = TreeNode(15)
Tree7 = TreeNode(7)
Tree9 = TreeNode(9)

Tree20 = TreeNode(20)
Tree20.left = Tree15
Tree20.right = Tree7

Tree = TreeNode(3)
Tree.left = Tree9
Tree.right = Tree20

def isBalanced(root):

#    import ipdb;ipdb.set_trace()
    def recur(root):
        if not root: return 0
        left = recur(root.left)
        if left == -1: return -1
        right = recur(root.right)
        if right == -1: return -1
        return max(left, right) +1 if abs(left - right) < 2 else -1

    return recur(root) != -1

print(isBalanced(Tree))

def isBalanced1(self, root):

    def check(root):
        if root is None:
            return 0
        left  = check(root.left)
        right = check(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return check(root) != -1


def isBalanced2(self, root):
    stack, node, last, depths = [], root, None, {}
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack[-1]
            if not node.right or last == node.right:
                node = stack.pop()
                left, right  = depths.get(node.left, 0), depths.get(node.right, 0)
                if abs(left - right) > 1: return False
                depths[node] = 1 + max(left, right)
                last = node
                node = None
            else:
                node = node.right
    return True
