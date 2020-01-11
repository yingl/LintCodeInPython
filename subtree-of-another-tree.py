"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param s: the s' root
    @param t: the t' root
    @return: whether tree t has exactly the same structure and node values with a subtree of s
    """
    def isSubtree(self, s, t):
        # Write your code here
        if not s:
            return False
        if self.isSameTree(s, t) \
           or self.isSubtree(s.left, t) \
           or self.isSubtree(s.right, t):
            return True
        return False
        
    def isSameTree(self, s, t):
        if s and t:
            if s.val != t.val:
                return False
        elif not (s or t):
            return True
        else:
            return False
        return self.isSameTree(s.left, t.left) \
               and self.isSameTree(s.right, t.right)
  
# easy: https://www.lintcode.com/problem/subtree-of-another-tree/
