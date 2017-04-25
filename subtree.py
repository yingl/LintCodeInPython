# coding: utf-8

class Solution:
    # @param T1, T2: The roots of binary tree.
    # @return: True if T2 is a subtree of T1, or false.
    def isSubtree(self, T1, T2):
        # write your code here
        if (T1 is None) and (T2 is None):
            return True
        elif T1 is None:
            return False
        elif T2 is None:
            return True
        if T1.val != T2.val:
            return self.isSubtree(T1.left, T2) or self.isSubtree(T1.right, T2)
        else:
            if self.isSametree(T1, T2):
                return True
            else:
                return self.isSubtree(T1.left, T2) or \
                    self.isSubtree(T1.right, T2)

    def isSametree(self, T1, T2):
        if (T1 is None) and (T2 is None):
            return True
        if T1 is None:
            return False
        if T2 is None:
            return False
        if T1.val == T2.val:
            return self.isSametree(T1.left, T2.left) and \
                self.isSametree(T1.right, T2.right)
        else:
            return False

# easy: http://lintcode.com/zh-cn/problem/subtree/
