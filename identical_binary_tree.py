# coding: utf-8

class Solution:
    """
    @param a, b, the root of binary trees.
    @return true if they are identical, or false.
    """
    def isIdentical(self, a, b):
        # Write your code here
        if not (a or b):
            return True
        if a and b:
            if a.val == b.val:
                return self.isIdentical(a.left, b.left) and self.isIdentical(a.right, b.right)
        return False

# easy: http://lintcode.com/zh-cn/problem/identical-binary-tree/
