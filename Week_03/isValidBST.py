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


def isValidBST(root):
    #recursion
    # 时间复杂度 : O(n)O(n)，其中 nn 为二叉树的节点个数。在递归调用的时候二叉树的每个节点最多被访问一次，因此时间复杂度为 O(n)O(n)。
    # 空间复杂度 : O(n)O(n)，其中 nn 为二叉树的节点个数。递归函数在递归过程中需要为每一层递归函数分配栈空间，所以这里需要额外的空间且该空间取决于递归的深度，即二叉树的高度。最坏情况下二叉树为一条链，树的高度为 nn ，递归最深达到 nn 层，故最坏情况下空间复杂度为 O(n)O(n) 。

    def helper(root, lower=float('-inf'), upper=float('inf')):
        if not root:
            return False
        val = root.val

        if val <= lower or val >= upper:
            return False
        if not helper(node.right, val, upper):
            return False
        if not helper(node.left, lower, val):
            return False

        return True

    return helper(root)


def isValidBST(root):
    #BST 中序遍历: 基于方法一中提及的性质，我们可以进一步知道二叉搜索树「中序遍历」得到的值构成的序列一定是升序的，这启示我们在中序遍历的时候实时检查当前节点的值是否大于前一个中序遍历到的节点的值即可
    stack, inorder = [], float('-inf')

    import ipdb;ipdb.set_trace()
    while stack or root:
        while root:
            stack.append(root) # root 入栈
            root = root.left #root 左孩子入栈
        root = stack.pop()
        if root.val <= inorder:
            return False
        inorder = root.val
        root = root.right #root 右孩子入栈
    return True

print(isValidBST(Tree))
