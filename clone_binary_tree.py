# coding: utf-8

class Solution:
    """
    @param {TreeNode} root: The root of binary tree
    @return {TreeNode} root of new tree
    """
    def cloneTree(self, root):
        # Write your code here
        new_root = None
        if root:
            new_root = TreeNode(root.val)
            if root.left:
                new_root.left = self.cloneTree(root.left)
            if root.right:
                new_root.right = self.cloneTree(root.right)
        return new_root

# easy: http://lintcode.com/zh-cn/problem/clone-binary-tree/
