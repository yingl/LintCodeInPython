"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """

    def twoSum(self, root, n):
        # write your code here
        if root:
            ret = [-1, n]
            self._twoSum(root, root, n, ret)
            if (ret[0] + ret[1]) == n:
                return ret
        return None
        
    def _twoSum(self, root, node, n, ret):
        if not node:
            return
        if self.exists(root, n - node.val):
            ret[0] = node.val
            ret[1] = n - node.val
        else:
            self._twoSum(root, node.left, n, ret)
            self._twoSum(root, node.right, n, ret)
    
    def exists(self, root, val):
        if not root:
            return False
        if root.val == val:
            return True
        elif root.val > val:
            return self.exists(root.left, val)
        else:
            return self.exists(root.right, val)
            
# easy: https://www.lintcode.com/problem/two-sum-iv-input-is-a-bst/
