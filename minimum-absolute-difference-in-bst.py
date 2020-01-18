"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root
    @return: the minimum absolute difference between values of any two nodes
    """
    def getMinimumDifference(self, root):
        # Write your code here
        self.vals = []
        self.inOrder(root)
        ret = self.vals[-1] - self.vals[0]
        for i in range(1, len(self.vals)):
            if (self.vals[i] - self.vals[i - 1]) < ret:
                ret = self.vals[i] - self.vals[i - 1]
        return ret
        
    def inOrder(self, root):
        if not  root:
            return
        if root.left:
            self.inOrder(root.left)
        self.vals.append(root.val)
        if root.right:
            self.inOrder(root.right)

# easy: https://www.lintcode.com/problem/minimum-absolute-difference-in-bst/
