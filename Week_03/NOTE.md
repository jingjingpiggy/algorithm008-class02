学习笔记
第三周 第7课 泛型递归、树的递归

二叉搜索树: 左子树小于根节点，右子树大于根节点
树的遍历： 前序、中序、后续
1. def preorder(self, root):
    if root:
        self.traverse_path.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

2. def inorder(self, root):
    if root:
        self.inorder(root.left)
        self.traverse_path.append(root.val)
        self.inorder(root.right)

3. def postorder(root):
    if root:
        self.postorder(root.left)
        self.postorder(root.right)
        self.traverse_path.append(root.val)

Python 代码模板:
def recursion(level, param1, param2, ...):
    # recursion terminator # 递归终结条件
    if level > MAX_LEVEL:
        process_result
        return

    # process logic in current level #处理当前层逻辑
    process(level, data...)

    # drill down 下探到下一层
    self.recursion(level+1, p1, ...)

    # reverse the current level status if needed 清理当前层 一般处理全局变量


第八课 分治、回溯
本质：一种递归，本质就是找它的重复性，分解问题，组合问题
divide -> conquer -> merge

1) 分治
def divide_conquer(problem, param1, param2,...):
    # recursion terminator
    if problem is None:
        print result
        return

    # prepare data
    data = prepare_data(problem)
    subproblems = split_problem(problem, data)

    # conquer subproblems
    subresult1 = self.divide_conquer(subproblems[0], p1, ...)
    subresult2 = self.divide_conquer(subproblems[1], p1, ...)
    subresult3 = self.divide_conquer(subproblems[2], p1, ...)

    # process and generate the final result
    result = process_result(subresult1, subresult2, subresult3, ...)

    # revert the current level states


2) 回溯: 不断的在每一层一个一个的去尝试，看这个方法行不行，最典型的应用：八皇后 数独。



Day16:
https://leetcode-cn.com/problems/add-strings/
https://leetcode-cn.com/problems/number-of-burgers-with-no-waste-of-ingredients/
https://leetcode-cn.com/problems/spiral-matrix/

Day17:
https://leetcode-cn.com/problems/ti-huan-kong-ge-locf/
https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-icof/
https:////leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/

Day18:
https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/

Day19:
https://leetcode-cn.com/problems/number-of-islands/

Day21:
https://leetcode-cn.com/problems/valid-anagram/description/

Day22:
https://leetcode-cn.com/problems/climbing-stairs/

Day23:
https://leetcode-cn.com/problems/minimum-genetic-mutation/#/description

Day24:
https://leetcode-cn.com/problems/minesweeper/

Day25:
https://leetcode-cn.com/problems/majority-element/
摩尔投票法，多数投票法：如何在任意多的候选人中（选票无序），选出获得票数最多的那个

算法可以分为两个阶段：
    1. 对抗阶段：分属两个候选人的票数进行两两对抗抵消
    2. 计数阶段：计算对抗结果中最后留下的候选人票数是否有效

根据上述的算法思想，我们遍历投票数组，将当前票数最多的候选人与其获得的（抵消后）票数分别存储在 major 与 count 中。

当我们遍历下一个选票时，判断当前 count 是否为零：

若 count == 0，代表当前 major 空缺，直接将当前候选人赋值给 major，并令 count++
若 count != 0，代表当前 major 的票数未被完全抵消，因此令 count--，即使用当前候选人的票数抵消 major 的票数
