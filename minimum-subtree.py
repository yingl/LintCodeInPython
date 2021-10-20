"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        ret = None
        if root:
            di = {None: 0}
            self.sum(root, di)
            s = max(di.values())
            for k, v in di.items():
                if k:
                    if v <= s:
                        s = v
                        ret = k
        return ret

    def sum(self, root, di):
        if not root:
            return 0
        if root not in di:
            di[root] = self.sum(root.left, di) + self.sum(root.right, di) + root.val
        return di[root]

      
# easy: https://www.lintcode.com/problem/596/
