class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

# DFS
class Solution:
    def hasPathSum(self, root, sums):
        if not root: return False
        if not root.left and not root.right:
            return sums = root.val
        return self.hasPathSum(root.left, sums-root.val) or self.hasPathSum(root.right, sums-root.val)
