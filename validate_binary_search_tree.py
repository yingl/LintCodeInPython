# coding: utf-8

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """  
    def isValidBST(self, root):
        # write your code here
        if root is None:
            return True
        return self.check(root.left, root.val, None) and \
                self.check(root.right, None, root.val)
        
    def check(self, root, left_max, right_min):
        if root is None:
            return True
        if left_max and (root.val >= left_max):
            return False
        if right_min and (root.val <= right_min):
            return False
        return self.check(root.left, root.val, right_min) and \
                self.check(root.right, left_max, root.val)

# medium: http://lintcode.com/zh-cn/problem/validate-binary-search-tree/
