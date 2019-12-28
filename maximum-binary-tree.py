"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param nums: an array
    @return: the maximum tree
    """
    def constructMaximumBinaryTree(self, nums):
        # Write your code here
        return self._constructMaximumBinaryTree(nums, 0, len(nums) - 1)
        
    def _constructMaximumBinaryTree(self, nums, start, end):
        if start > end:
            return None
        elif start == end:
            return TreeNode(nums[start])
        else:
            _max = nums[start]
            idx = start
            for i in range(start + 1, end + 1):
                if nums[i] > _max:
                    _max = nums[i]
                    idx = i
            ret = TreeNode(_max)
            ret.left = self._constructMaximumBinaryTree(nums, start, idx - 1)
            ret.right = self._constructMaximumBinaryTree(nums, idx + 1, end)
            return ret

# easy: https://www.lintcode.com/problem/maximum-binary-tree/
