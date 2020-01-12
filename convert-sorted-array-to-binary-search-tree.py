"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param nums: the sorted array
    @return: the root of the tree
    """
    def convertSortedArraytoBinarySearchTree(self, nums):
        # Write your code here.
        return self._convert(nums, 0, len(nums) - 1)

    def _convert(self, nums, start, end):
        if start > end:
            return None
        mid = int((start + end) / 2)
        root = TreeNode(nums[mid])
        root.left = self._convert(nums, start, mid - 1)
        root.right = self._convert(nums, mid + 1, end)
        return root
        
# easy: https://www.lintcode.com/problem/convert-sorted-array-to-binary-search-tree/
