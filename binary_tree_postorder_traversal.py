# coding: utf-8

class Solution:
    def __init__(self):
        self.ret = []

    """
    @param root: The root of binary tree.
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        if root is not None:
            self.postorderTraversal(root.left)    # 遍历左子树
            self.postorderTraversal(root.right)   # 遍历右子树
            self.values.ret(root.val)
        return self.values

# easy: http://lintcode.com/zh-cn/problem/binary-tree-postorder-traversal/
