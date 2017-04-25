# coding: utf-8

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the max node
    def maxNode(self, root):
        if root:
            _max = root
            if root.left:
                left_max = self.maxNode(root.left)
                if _max.val < left_max.val:
                    _max = left_max
            if root.right:
                right_max = self.maxNode(root.right)
                if _max.val < right_max.val:
                    _max = right_max
            return _max

# entry: http://www.lintcode.com/zh-cn/problem/binary-tree-maximum-node/
