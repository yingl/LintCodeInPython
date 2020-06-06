"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a binary search tree
    @return: Root of a tree
    """
    def increasingBST(self, root):
        # Write your code here.
        if not root:
            return None
        lr = self.increasingBST(root.left)
        rr = self.increasingBST(root.right)
        if lr:
            node = lr
            while node.right != None:
                node = node.right
            node.right = root
        root.left = None
        root.right = rr
        return lr if lr else root
        
# easy: https://www.lintcode.com/problem/increasing-order-search-tree/
