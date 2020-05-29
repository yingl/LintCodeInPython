"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: 
    @return: the length of the longest path where each node in the path has the same value
    """
    def longestUnivaluePath(self, root):
        # Write your code here
        '''
        就像网友所说，这题easy难度的确是膨胀了...
        简说下思路：
        1. 5-5-5路径长度是2，5路径长度是0。
        2. 要处理2种情况：1）路径不经过当前节点；2）路径经过当前节点。
        '''
        self.ret = 0
        self._longestUnivaluePath(root)
        return self.ret
        
    def _longestUnivaluePath(self, node):
        if not node:
            return 0
        ll = self._longestUnivaluePath(node.left)
        lr = self._longestUnivaluePath(node.right)
        to_left, to_right = 0, 0
        if node.left and (node.left.val == node.val):
            to_left = ll + 1
        if node.right and (node.right.val == node.val):
            to_right = lr + 1
        self.ret = max(self.ret, to_left + to_right) # 处理左到右经过当前节点的情况
        return max(to_left, to_right) # 处理需要继续向上的情况

# https://www.lintcode.com/problem/longest-univalue-path/
