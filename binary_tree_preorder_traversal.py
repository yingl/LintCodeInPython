# coding: utf-8

class Solution:
    def __init__(self):
        self.ret = []

    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        if root is not None:
            self.ret.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
        return self.ret

# easy: http://lintcode.com/problem/binary-tree-preorder-traversal
