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
    @return: the maximum weight node
    """
    def findSubtree(self, root):
        # write your code here
        ret = None
        if root:
            di = {None: 0}
            self.sum(root, di)
            s = 0
            for k, v in di.items():
                if v >= s:
                    s = v
                    ret = k
        return ret

    def sum(self, root, di):
        if not root:
            return 0
        if root not in di:
            di[root] = self.sum(root.left, di) + self.sum(root.right, di) + root.val
        return di[root]
      
# easy: https://www.lintcode.com/problem/628
