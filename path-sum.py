"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the tree
    @param sum: the sum
    @return:  if the tree has a root-to-leaf path 
    """
    def pathSum(self, root, sum):
        # Write your code here.
        if not root:
            return False
        if (not root.left) and (not root.right):
            return root.val == sum
        b_left, b_right = False, False
        if root.left:
            b_left = self.pathSum(root.left, sum - root.val)
        if root.right:
            b_right = self.pathSum(root.right, sum - root.val)
        return b_left or b_right
            
        
# easy: https://www.lintcode.com/problem/path-sum/
