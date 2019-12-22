"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param t1: the root of the first tree
    @param t2: the root of the second tree
    @return: the new binary tree after merge
    """
    def mergeTrees(self, t1, t2):
        # Write your code here
        root = None
        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
        elif t1:
            root = TreeNode(t1.val)
            root.left = self.mergeTrees(t1.left, None)
            root.right = self.mergeTrees(t1.right, None)
        elif t2:
            root = TreeNode(t2.val)
            root.left = self.mergeTrees(t2.left, None)
            root.right = self.mergeTrees(t2.right, None)
        return root
            
# easy: https://www.lintcode.com/problem/merge-two-binary-trees/
