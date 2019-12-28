"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: t
    @return: the sum of all left leaves
    """
    def sumOfLeftLeaves(self, root):
        # Write your code here
        ret = [0] # 简化参数处理
        if root:
            self._sumOfLeftLeaves(ret, root, 0)
        return ret[0]
        
    def _sumOfLeftLeaves(self, ret, node, _dir):
        if not (node.left or node.right) and (_dir == -1):
            ret[0] += node.val
        if node.left:
            self._sumOfLeftLeaves(ret, node.left, -1)
        if node.right:
            self._sumOfLeftLeaves(ret, node.right, 1)
            
# easy: https://www.lintcode.com/problem/sum-of-left-leaves/
