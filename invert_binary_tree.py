# coding: utf-8

class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def invertBinaryTree(self, root):
        # write your code here
        if root is None:
            return
        root.left, root.right = root.right, root.left
        self.invertBinaryTree(root.left)
        self.invertBinaryTree(root.right)

# easy: http://lintcode.com/zh-cn/problem/invert-binary-tree/
