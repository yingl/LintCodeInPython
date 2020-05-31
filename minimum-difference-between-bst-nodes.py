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
    @return: the minimum difference between the values of any two different nodes in the tree
    """
    def minDiffInBST(self, root):
        # Write your code here
        li = []
        self.build_list(root, li)
        ret = li[1] - li[0]
        for i in range(2, len(li)):
            diff = li[i] - li[i - 1]
            if diff < ret:
                ret = diff
        return ret
        

    def build_list(self, root, li):
        if root:
            self.build_list(root.left, li)
            li.append(root.val)
            self.build_list(root.right, li)
            
# easy: https://www.lintcode.com/problem/minimum-difference-between-bst-nodes/
