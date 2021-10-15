"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree.
    @return: true if it is a mirror of itself, or false.
    """
    def isSymmetric(self, root):
        # write your code here
        if root:
            return self.checkSymmetric(root.left, root.right)
        return True

    def checkSymmetric(self, left, right):
        if left and right:
            if left.val == right.val:
                return self.checkSymmetric(left.left, right.right) and self.checkSymmetric(left.right, right.left)
            else:
                return False
        elif (not left) and (not right):
            return True
        return False

# easy: https://www.lintcode.com/problem/468/
