"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a root of binary tree
    @return: return a integer
    """
    def diameterOfBinaryTree(self, root):
        # write your code here
        # 根节点为root的二叉树的直径
        # max(root-left的直径, \
        #     root->right的直径, \
        #     root->left的最大深度 + root->right的最大深度)
        # 重点：此路径不一定会通过树根
        if not root:
            return 0
        left_dia = self.diameterOfBinaryTree(root.left)
        right_dia = self.diameterOfBinaryTree(root.right)
        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)
        return max(left_dia, right_dia, left_depth + right_depth)
        
    def depth(self, root):
        if not root:
            return 0
        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)
        return max(left_depth, right_depth) + 1
        
# easy: https://www.lintcode.com/problem/diameter-of-binary-tree/
