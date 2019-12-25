"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param t: the root of tree
    @return: return a string
    """
    def tree2str(self, t):
        # write your code here
        ret = []
        if t:
            ret.append(str(t.val))
            if t.left:
                ret.append('(')
                ret.extend(self.tree2str(t.left))
                ret.append(')')
            if t.right:
                if not t.left:
                    ret.extend(['(', ')'])
                ret.append('(')
                ret.extend(self.tree2str(t.right))
                ret.append(')')
        return ''.join(ret)

# easy: https://www.lintcode.com/problem/construct-string-from-binary-tree/
