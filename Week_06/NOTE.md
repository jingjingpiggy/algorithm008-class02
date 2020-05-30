学习笔记
第六周 第12课 动态规划
动态规划的实现及关键点
递归，分治：找到最近最简方法，将其拆解成可重复解决的问题；数学归纳法思想（抵制人肉递归的诱惑）
本质：寻找重复性-->计算机指令集只会if else

DP: 求一个最优解、最大值或者求一个最少的方式
simplifying a complicated problem by breaking it down into simpler subproblems (in a recursive manner)

Divide & Conquer + Optimal substructure: 分治+最优子结构
最优子结构：正因为有最优子结构，中间每一步只要保存最优的状态，不需要保存所有的状态，如果每一步都能存一个最优的值，最优的话就能推导出一个全局的最优的值。

关键点:
动态规划和递归或者分治没有根本上的区别(关键看有无最优的子结构)
共性：找到重复子问题
差异性：DP最优子结构、中途可以淘汰次优解,时间复杂度为多项式级别；傻递归或者傻分治，通常是指数级的时间复杂度。

实战1：
斐波那契额数列：傻递归时间复杂度O2^n, 自顶向下：递归+记忆化搜索，自底向上：见例题
Count the paths: 分治的办法
    向左走和向右走---一开始出发只有A和B两个格子可以走，那就转换成找B点的子问题的解和A点子问题的解.
    向左走、向右走、向斜对角走-----就转换成A点、B点和C点子问题的解

实战2：最长公共子序列
状态转移方程(DP方程):
    opt[i, j] = opt[i+1, j] + opt[i, j+1]
    完整逻辑：
        if a[i, j] == “空地”:
            opt[i,j] = opt[i+1, j] + opt[i, j+1]
        else:
            opt[i, j] = 0

例题之后总结动态规划的关键点：
1. 最优子结构 opt[n] = best_of(opt[n-1], opt[n-2], ...)
2. 存储中间状态: opt[i]
3. 地推公式（上面的DP方程）
    Fib: opt[i] = opt[n-1] + opt[n-2]
    二维路径: opt[i, j] = opt[i+1][j] + opt[i][j+1](且判断a[i, j]是否是空地)

实战3：三角形最小路径和
1. 暴力穷举:递归，n层: 每一层可以左或者右，O2^n
2. DP: a. 重复性(分治) problem(i, j) = min(sub(i+1, j), sub(i+1, j+1)) + a[i, j]
       b. 定义状态数组: f[i, j]
       c. DP方程: f[i, j] = min(f[i+1, j], f[i+1, j+1]) + a[i, j]


递归：从上到下
动态规划：从下到上找最优解


实战4：

实战5：打家劫舍


Day43: 打家劫舍
https://leetcode-cn.com/problems/house-robber/

Day 44: 零钱兑换
https://leetcode-cn.com/problems/coin-change/

Day 45: 三角形最小路径和
https://leetcode-cn.com/problems/triangle/description/

Day 47:
https://leetcode-cn.com/problems/burst-balloons/
https://leetcode-cn.com/problems/number-of-segments-in-a-string/

Day 48:
https://leetcode-cn.com/problems/maximal-square/

zoom:
leetcode91： https://leetcode-cn.com/problems/decode-ways/
面试题17. 16：https://leetcode-cn.com/problems/the-masseuse-lcci/


leetcode 博主:
https://leetcode-cn.com/u/liweiwei1419/ 
https://leetcode-cn.com/u/powcai/ 
https://leetcode-cn.com/u/sweetiee/ 
https://leetcode-cn.com/u/labuladong/
