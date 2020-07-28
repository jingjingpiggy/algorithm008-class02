class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth_dfs(root):
        if not root: return 0
        return 1 + max(self.maxDepth_dfs(root.left), self.maxDepth_dfs(root.right))


    def maxDepth_bfs(root):
        if not root: return 0

        level = 0
        from collections import deque

        queue = deque()
        queue.append(root)

        while queue:
            level += 1
            for i in range(len(queue)):
                cur = queue.popleft()
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)

        return level

    def maxDepth_bfs(root):
        if not root: return 0

        level = 0
        stack = [root]
        while stack:
            level += 1
            for i in range(len(stack))
            cur = stack.pop(0)
            if cur.left: stack.append(cur.left)
            if cur.right: stack.append(cur.right)

        return level
