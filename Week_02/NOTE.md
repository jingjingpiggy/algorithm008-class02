学习笔记
Day8: 错过299，290

重新启程：
第二周 第五课：
哈希表：也叫散列表，是根据关键码值而进行访问的数据结构，映射函数叫散列函数, 存放数据的数组叫哈希表。
哈希碰撞：
哈希map：哈希表+链表
平均时间复杂度，空间复杂度：search O1, insertion O1, Deletion O1;
最坏情况时间复杂度：哈希表的size太小了/哈希函数选的不好，哈希表退化成链表，复杂度变为 search On, insertion On, Deletion On
抽象出来的数据结构：map和set， python：dict和set
红黑树是严格平衡的：所有操作中，平均复杂度和最坏时间复杂度---search Ologn, insertion Ologn, Deletion Ologn

第二周 第六课:
一.堆 Heap: 可以迅速找到一堆树中的最大或者最小值的数据结构, 两者一般来说只能取其一.

将根节点最大的堆叫做大顶堆或大根堆，根节点最小的堆叫做小顶堆或小根堆。
常见的堆有二叉堆、斐波那契堆等。工业级比较牛逼的应用：斐波那契，时空复杂度更好。多叉树

假设是的大顶堆，常见的操作 API:
find-max: O1
delete-max: OlogN
insert(create): OlogN or O1

如果维护一个数组的话：需要排序，时间复杂度nlogn，删除时间复杂度也变差了。二叉堆的时间复杂度相对来说比较差，刚刚及格，实现起来比较容易，严格的斐波那契堆是时间复杂度是最高的。

1. 二叉堆性质：通过完全二叉树来实现：除了最下一层的叶子是不满的之外，上面的根和每一层都是满的。
二叉树不是二叉搜索树。堆也不是二叉搜索树。二叉搜索树要找最小值时间复杂度Ologn的
二叉堆（大顶）它满足下列性质：
1）是一个完全树
2）树中任意节点的值总是>=其子节点的值

完全二叉树存储：一般通过一维数组实现。在数组中的索引: 索引为i的左孩子的索引是 2*i+1; 索引为i的右孩子的结点索引是 2*i+2; 索引为i的父节点的索引是 floor((i-1)/2)

Insert 插入操作: 先比较 但不赋值，等比较到最后的时候再最后的位置赋值，这样就会少很多次赋值操作。
1) 新元素一律先插入到堆的尾部
2）一次向上调整整个堆的结构(一直到根即可), 最坏时间复杂度 是树的深度：二叉树就是log2n

Delete Max 删除堆顶操作:
1) 将堆尾元素替换到顶部（即对顶被替代删除掉）
2）一次从根部向下调整整个堆的结构（一直到堆尾即可）最坏的时间复杂度: OlongN

注意: 二叉堆是对（优先队列priority_queue）的一种常见且简单的实现；但并不是最优的实现。


二. 图的实现和特性
1. 图的属性和分类：
Graph(V, E)
V-vertex: 点
1) 度 - 入度和出度
2）点与点之间：联通与否

E-edge: 边
1) 有向和无向(单行线)
2）权重(边长)

图的表示和分类：邻接矩阵和邻接表，二维的数据结构
无向无权图(对称矩阵)，有向无权图，无向有全图 (对称矩阵)

2. 基于图相关的算法:
DFS: visited-和树中的DFS最大区别, 因为树中不存在环路, 所以可以没有visited, 递归
BFS: visited also

1). 连通图个数: https://leetcode-cn.com/problems/number-of-islands/
2). 拓扑排序: https://zhuanlan.zhihu.com/p/34871092
3). 最短路径: https://wwww.bilibili.com/video/av25829980?from=search&seid=13391343514095937158
4). 最小生成树: https://www.bilibili.com/video/av84820276?from=search&seid=17476598104352152051

Day8
https://leetcode-cn.com/problems/bulls-and-cows /
https://leetcode-cn.com/problems/word-pattern /

Day9:
https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/
https://leetcode-cn.com/problems/is-subsequence/
https://leetcode-cn.com/problems/get-kth-magic-number-lcci/

Day10:
https://leetcode-cn.com/problems/remove-outermost-parentheses/
https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/

DAY11:
https://leetcode-cn.com/problems/fizz-buzz/
https://leetcode-cn.com/problems/add-digits/
https://leetcode-cn.com/problems/move-zeroes/

DAY12:
https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/
https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree/
https://leetcode-cn.com/problems/balanced-binary-tree/
二叉树，多叉树的遍历方法: 递归、BFS 和DFS

+DAY13:
+https://leetcode-cn.com/problems/zero-matrix-lcci/
+https://leetcode-cn.com/problems/minimum-absolute-difference/
+https://leetcode-cn.com/problems/diameter-of-binary-tree/

简单
写一个关于 HashMap 的小总结。
说明：对于不熟悉 Java 语言的同学，此项作业可选做。
https://leetcode-cn.com/problems/valid-anagram/description/
https://leetcode-cn.com/problems/two-sum/description/
https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/description/
HeapSort ：自学 https://www.geeksforgeeks.org/heap-sort/

中等
https://leetcode-cn.com/problems/group-anagrams/
https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/
https://leetcode-cn.com/problems/chou-shu-lcof/
https://leetcode-cn.com/problems/top-k-frequent-elements/
