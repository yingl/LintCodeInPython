# coding: utf-8

class Solution:
    """
    @param A: a list of integer
    @return: a tree node
    """
    def sortedArrayToBST(self, A):
        # write your code here
       if not A:
            return None
        return self._sortedArrayToBST(A, 0, len(A))

    def _sortedArrayToBST(self, array, start, end):
        if start >= end:
            return None
        mid = (start + end) / 2
        root = TreeNode(array[mid])
        root.left = self._sortedArrayToBST(array, start, mid)   # 生成左子树
        root.right = self._sortedArrayToBST(array, mid + 1, end)    # 生成右子树
        return root

# easy: http://lintcode.com/problem/convert-sorted-array-to-binary-search-tree-with-minimal-height
