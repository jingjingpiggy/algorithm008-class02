class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

# DFS
# 时间复杂度ON
# 空间复杂度OH,树的高度最坏情况下空间复杂度为ON，平均情况下树的高度与节点数的对数正相关OlogN
class Solution:
    def hasPathSum(self, root, sums):
        if not root: return False
        if not root.left and not root.right:
            return sums = root.val
        return self.hasPathSum(root.left, sums-root.val) or self.hasPathSum(root.right, sums-root.val)


#BFS same as stack=[]
class Solution:
    def hasPathSum(self, root, sums):
        from collections import deque
        if not root: return False
    
        que = deque()
        que.append((root, root.val))
        while que:
            cur, val = que.popleft()
            if not cur.left and not cur.right and val == sums:
                return True
            if cur.left:
                que.append((cur.left, val+cur.left.val))
            if cur.right:
                que.append((cur.right, val+cur.right.val))
        return False
