"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: root of the given tree
    @return: whether it is a mirror of itself 
    """
    def isSymmetric(self, root):
        # Write your code here
        if not root:
            return True
        return self.compare(root.left, root.right)
        
    def compare(self, left, right):
        if (not left) and (not right):
            return True
        elif left and right:
            return self.compare(left.left, right.right) and self.compare(left.right, right.left)
        else:
            return False

# easy: https://www.lintcode.com/problem/symmetric-tree/
