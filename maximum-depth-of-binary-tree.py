# coding: utf-8

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """ 
    def maxDepth(self, root):
        # write your code here
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# easy: http://lintcode.com/zh-cn/problem/maximum-depth-of-binary-tree/
