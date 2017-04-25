# coding: utf-8

class Solution:
    """
    @param root: The root of the binary search tree.
    @param k1 and k2: range k1 to k2.
    @return: Return all keys that k1<=key<=k2 in ascending order.
    """     
    def searchRange(self, root, k1, k2):
        # write your code here
        ret = []
        if root:
            '''
            判断搜索范围：
            1. 根节点在k1、k2之间，符合条件，加入返回集合。
            2. 如果根节点大于等于k1，搜索左子树。
            2. 如果根节点小于等于k1，搜索右子树。
            '''
            if (root.val >= k1) and (root.val <= k2):
                ret.append(root.val)
            if root.val >= k1:
                ret.extend(self.searchRange(root.left, k1, k2))
            if root.val <= k2:
                ret.extend(self.searchRange(root.right, k1, k2))
        ret.sort()
        return ret

# medium: http://lintcode.com/zh-cn/problem/search-range-in-binary-search-tree/
