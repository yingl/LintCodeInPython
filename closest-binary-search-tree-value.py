"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        if root.val > target:
            if root.left:
                val = self.closestValue(root.left, target)
                return val if abs(root.val - target) > abs(val - target) else root.val
        elif root.val < target:
            if root.right:
                val = self.closestValue(root.right, target)
                return val if abs(root.val - target) > abs(val - target) else root.val
        return root.val

# easy: https://www.lintcode.com/problem/closest-binary-search-tree-value/
