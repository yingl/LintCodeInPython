"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the binary tree of the  root
    @return: return a list of double
    """
    def averageOfLevels(self, root):
        # write your code here
        ret = []
        levels = [[root], []]
        curr = 0
        while levels[curr]:
            s = 0
            _next = 1 - curr
            for node in levels[curr]:
                s += node.val
                if node.left:
                    levels[_next].append(node.left)
                if node.right:
                    levels[_next].append(node.right)
            ret.append(s / len(levels[curr]))
            levels[curr].clear()
            curr = _next
        return ret
        
# easy: https://www.lintcode.com/problem/average-of-levels-in-binary-tree/description
