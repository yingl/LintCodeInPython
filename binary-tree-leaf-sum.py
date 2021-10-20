"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: An integer
    """
    def leafSum(self, root):
        # write your code here
        if not root:
            return 0
        if not (root.left or root.right):
            return root.val
        r = 0
        if root.left:
            r += self.leafSum(root.left)
        if root.right:
            r += self.leafSum(root.right)
        return r

# easy: https://www.lintcode.com/problem/481
