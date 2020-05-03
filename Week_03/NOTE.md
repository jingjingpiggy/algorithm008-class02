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
