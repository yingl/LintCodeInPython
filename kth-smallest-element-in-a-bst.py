"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        less = self.count(root.left) # 比root小的元素的数量
        if less == (k - 1):
            return root.val
        elif less < (k - 1):
            return self.kthSmallest(root.right, k - less - 1)
        else:
            return self.kthSmallest(root.left, k)
        
    def count(self, root):
        if not root:
            return 0
        return 1 + self.count(root.left) + self.count(root.right)
        
# medium: https://www.lintcode.com/problem/kth-smallest-element-in-a-bst/
