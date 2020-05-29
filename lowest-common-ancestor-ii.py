"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        # write your code here
        s = set([])
        while A:
            s.add(A)
            A = A.parent
        while B:
            if B in s:
                return B
            B = B.parent
        return None

# easy: https://www.lintcode.com/problem/lowest-common-ancestor-ii/
