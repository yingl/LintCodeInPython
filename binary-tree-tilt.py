"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root
    @return: the tilt of the whole tree
    """
    def findTilt(self, root):
        # Write your code here
        ret = [0] # 方便传参数
        self.traversal(root, ret)
        return ret[0]
        
    def traversal(self, node, ret):
        if node:
            left_sum = self.getSum(node.left)
            right_sum = self.getSum(node.right)
            ret[0] += abs(left_sum - right_sum)
            self.traversal(node.left, ret)
            self.traversal(node.right, ret)
        
    def getSum(self, node):
        if not node:
            return 0
        else:
            return node.val + self.getSum(node.left) + self.getSum(node.right)

# easy: https://www.lintcode.com/problem/binary-tree-tilt/
