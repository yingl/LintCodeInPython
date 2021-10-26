"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        # We can utilize the feature of BST!
        if not root:
            return None
        if root.val > p.val:
            return self.inorderSuccessor(root.left, p) or root
        else:
            return self.inorderSuccessor(root.right, p)
          
# medium: https://www.lintcode.com/problem/448
