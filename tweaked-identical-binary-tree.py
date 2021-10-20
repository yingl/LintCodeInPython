"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param a: the root of binary tree a.
    @param b: the root of binary tree b.
    @return: true if they are tweaked identical, or false.
    """
    def isTweakedIdentical(self, a, b):
        # write your code here
        if a and b:
            if a.val == b.val:
                f1 = self.isTweakedIdentical(a.left, b.left) and self.isTweakedIdentical(a.right, b.right)
                f2 = self.isTweakedIdentical(a.left, b.right) and self.isTweakedIdentical(a.right, b.left)
                return f1 or f2
        elif not (a or b):
            return True
        return False

# easy: https://www.lintcode.com/problem/470
