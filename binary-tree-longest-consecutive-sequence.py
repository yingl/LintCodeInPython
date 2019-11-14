class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive(self, root):
        # write your code here
        return Solution.longest(root, None, 0)

    @staticmethod
    def longest(node, parent, curr_len):
        if not node:
            return 0
        if parent and ((parent.val + 1) == node.val):
            curr_len = curr_len + 1
        else:
            curr_len = 1
        left_len = Solution.longest(node.left, node, curr_len)
        right_len = Solution.longest(node.right, node, curr_len)
        return max(curr_len, max(left_len, right_len))
        
# easy: https://www.lintcode.com/problem/binary-tree-longest-consecutive-sequence/
