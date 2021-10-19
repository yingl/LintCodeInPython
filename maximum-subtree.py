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
        di = {None: 0}
        return self.find(root, di)

    def find(self, root, di):
        if not root:
            return None
        nl = self.find(root.left, di)
        nr = self.find(root.right, di)
        s = self.sum(root, di)
        sl = di[nl]
        sr = di[nr]
        if nl and nr:
            if s >= max(sl, sr):
                return root
            else:
                return nl if sl > sr else nr
        elif nl: # right is None
            return root if s >= sl else nl;
        elif nr: # left is None
            return root if s >= sr else nr;
        else:
            return root

    def sum(self, root, di):
        if root not in di:
            di[root] = self.sum(root.left, di) + self.sum(root.right, di) + root.val
        return di[root]
      
# easy: https://www.lintcode.com/problem/628
