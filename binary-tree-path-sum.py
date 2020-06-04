"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum(self, root, target):
        # write your code here
        ret = []
        self._binaryTreePathSum(ret, [], root, target)
        return ret
        
    def _binaryTreePathSum(self, ret, path, node, target):
        if not node:
            return
        path.append(node.val)
        if not (node.left or node.right):
            if node.val == target:
                ret.append([])
                ret[-1].extend(path)
        if node.left:
            self._binaryTreePathSum(ret, path, node.left, target - node.val)
            path.pop()
        if node.right:
            self._binaryTreePathSum(ret, path, node.right, target - node.val)
            path.pop()

# easy: https://www.lintcode.com/problem/binary-tree-path-sum/
