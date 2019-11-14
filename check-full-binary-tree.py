"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given tree
    @return: Whether it is a full tree
    """
    def isFullTree(self, root):
        # write your code here
        if not root:
            return None
        if (root.left == None) and (root.right == None): # 都为空的话没事
            return True
        elif (root.left != None) and (root.right != None): # 需要递归分别检查左右子树
            is_full = self.isFullTree(root.left)
            if not is_full:
                return False
            is_full = self.isFullTree(root.right)
            return is_full
        else:
            return False

# medium: https://www.lintcode.com/problem/check-full-binary-tree
