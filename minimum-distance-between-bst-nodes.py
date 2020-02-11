"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

def search(root, vals):
    if not root:
        return
    search(root.left, vals)
    vals[0] = min(vals[0], abs(root.val - vals[1]))
    vals[1] = root.val
    search(root.right, vals)

class Solution:
    """
    @param root:  a Binary Search Tree (BST) with the root node
    @return: the minimum difference
    """
    def minDiffInBST(self, root):
        # Write your code here.
        if (not root) or (not (root.left or root.right)):
            return 0
        vals = [4294967296, 4294967296] # [返回值，上一个节点的值]
        search(root, vals)
        return vals[0]

# easy: https://www.lintcode.com/problem/minimum-distance-between-bst-nodes/
