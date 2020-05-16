学习笔记

第四周 第10课 深度优先搜索和广度优先搜索
1. 深度优先
2. 广度优先
3. 优先级优先: 启发式搜索，估价函数以及搜索的效率问题更多的是深度学习，各种推荐算法，高级的搜索算法。

1). 深度优先 栈
def dfs(node):
    # 二叉树
    if node in visited:
        return
    visited.add(node)
    dfs(node.left)
    def(node.right)

visited = set()
def dfs(node, visited):
    # 多叉树
    if node in visited:
        # already visited
        return
    visited.add(node)

    # process current node here
    for next_node in node.children():
        if not next_node in visited:
            dfs(next_node, visited)


def dfs(tree):
    # 非递归写法
    if tree.root is None:
        return []

    visited, stack = [], [tree.root]
    while stack:
        node = stack.pop()
        visited.add(node)

        process(node)
        nodes = generate_related_nodes(node)
        stack.push(nodes)

    # other processing work

2) 广度优先 队列
地震，水滴，各种波纹
def bfs(graph, start, end):
    queue = []
    queue.append([start])
    visited.add(start)

    while queue:
        node = queue.pop()
        visited.add(node)

        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes)



第四周 第10课 贪心算法
贪心算法是一种在每一步选择中都采取在当前状态下最好或最有（即最有利）的选择,从而希望导致结果是全局最好或最有的算法
贪心算法与动态规划的不同在于：它对每个子问题的解决方案都做出选择，不能回退。动态规划则会保存以前的运算结果，并根据以前的记过对当前进行选择，有回退功能。

贪心：当下做局部最优判断
回溯：能够回退
动态规划：最优判断 + 回退

贪心法可以解决一些最优化问题，如：求图中的最小生成树、求哈夫曼编码等。然而对于工程和生活中的问题，贪心法一般不能得到我们所要求的答案
一旦一个问题可以通过贪心法来求解，那么贪心法一般是解决这个问题的最好办法。
由于贪心法的高效性以及其所求得的大胆比较接近最优结果，贪心法也可以用作辅助算法或者直接解决一些要求结果不特别精确的问题。

适用贪心算法的情况：
1. 简单的说，问题能够分解成子问题来解决，子问题的最优解能够递推到最终问题的最优解。这种子问题最优解成为最优子结构。
2. 贪心算法与动态规划的不同在于：它对每个子问题的解决方案都做出选择，不能回退。动态规划则会保存以前的运算结果，并根据以前的记过对当前进行选择，有回退功能。


第四周 第11课 二分查找
二分查找的实现、特性及实战题目解析

1. 目标函数单调性（单调递增或者递减）
2. 存在上下界（boudned）
3. 能够通过索引访问（index accessible）

代码模板:
left, right = 0, len(array) - 1
while left <= right:
    if array[mid] == target:
        return/break
    elif array[mid] < target:
        left = mid + 1
    else:
        right = mid -

时间复杂度Ologn

Day 29
https://leetcode-cn.com/problems/binary-tree-level-order-traversal/#/description

Day 30:
https://leetcode-cn.com/problems/sqrtx/

Day 31:
https://leetcode-cn.com/problems/assign-cookies/description/

Day 32:
https://leetcode-cn.com/problems/search-in-rotated-sorted-array/

Day 33:
https://leetcode-cn.com/problems/jump-game-ii/
