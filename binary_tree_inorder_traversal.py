# -*- coding: utf-8 -*-

class Solution:
    def __init__(self):
        self.ret = []

    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        if root is not None:
            self.inorderTraversal(root.left)    # 遍历左子树
            self.ret.append(root.val)
            self.inorderTraversal(root.right)   # 遍历右子树
        return self.ret