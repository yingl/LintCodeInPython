# coding: utf-8

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        if not root:
            return True
        else:
            if abs(self._isBalanced(root.left) - self._isBalanced(root.right)) <= 1:
                return self.isBalanced(root.left) and self.isBalanced(root.right)
            else:
                return False

    def _isBalanced(self, root):
        if not root:
            return 0
        return 1 + max(self._isBalanced(root.left), self._isBalanced(root.right))

# easy: http://lintcode.com/zh-cn/problem/balanced-binary-tree/
