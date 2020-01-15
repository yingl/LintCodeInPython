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
    @return: the second minimum value in the set made of all the nodes' value in the whole tree
    """
    def findSecondMinimumValue(self, root):
        # Write your code here
        # 深入领会题目：这个结点的值不大于它的两个子结点
        if (not root) or (not (root.left or root.right)):
            return -1
        left_val, right_val = -1, -1
        if root.left:
            left_val = root.left.val
            if left_val == root.val:
                left_val = self.findSecondMinimumValue(root.left)
        if root.right:
            right_val = root.right.val
            if right_val == root.val:
                right_val = self.findSecondMinimumValue(root.right)
        if (left_val != -1) and (right_val != -1):
            return min(left_val, right_val)
        if left_val != -1:
            return left_val
        return right_val

# easy: https://www.lintcode.com/problem/second-minimum-node-in-a-binary-tree/
