# coding: utf-8

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """ 
    def minDepth(self, root):
        # write your code here
        self.min_depth = 2147483647
        if not root:
            return 0
        self.dfs(root, 1)
        return self.min_depth

    def dfs(self, root, depth):
        if not (root.left or root.right):
            if depth < self.min_depth:
                self.min_depth = depth
        else:
            if root.left:
                self.dfs(root.left, depth + 1)
            if root.right:
                self.dfs(root.right, depth + 1)

# easy: http://lintcode.com/zh-cn/problem/minimum-depth-of-binary-tree/
