#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Li jinjing <lijinjing@gmail.com>
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        def make_tree(start_index, end_index):
            if start_index > end_index: return

            mid_index = (start_index + end_index) // 2
            tree_root = TreeNode(nums[mid_index])
            tree_root.left = make_tree(start_index, mid_index-1)
            tree_root.right = make_tree(mid_index+1, end_index)

            return tree_root
        return make_tree(0, len(nums)-1)
