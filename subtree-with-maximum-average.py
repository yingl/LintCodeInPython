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
    @return: the root of the maximum average of subtree
    """
    def findSubtree2(self, root):
        # write your code here
        if not root:
            return None
        di = {None: [0, 0]}
        self.calc_average(di, root)
        ret, a = None, 0
        for k, v in di.items():
            if not ret:
                ret, a = k, v[0]
            else:
                if v[0] > a:
                    a = v[0]
                    ret = k
        return ret

    def calc_average(self, di, node):
        if not node:
            return
        if node.left not in di:
            self.calc_average(di, node.left)
        la, lc = di[node.left]
        if node.right not in di:
            self.calc_average(di, node.right)
        ra, rc = di[node.right]
        cc = lc + rc + 1
        ca = (la * lc + ra * rc + node.val) / cc
        di[node] = [ca, cc]
            
# easy: https://www.lintcode.com/problem/597/
