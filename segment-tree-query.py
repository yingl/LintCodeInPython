# coding: utf-8

class Solution: 
    # @param root, start, end: The root of segment tree and 
    #                          an segment / interval
    # @return: The maximum number in the interval [start, end]
    def query(self, root, start, end):
        # write your code here
        if (root.start == start) and (root.end == end):
            return root.max
        mid = (root.start + root.end) / 2 # 后面根据mid区分去左右子树
        if start > mid:
            return self.query(root.right, start, end)
        elif end <= mid:
            return self.query(root.left, start, end)
        else: # start <= mid and end > mid
            left_max = self.query(root.left, start, mid)
            right_max = self.query(root.right, mid + 1, end)
            return max(left_max, right_max)

# medium: http://lintcode.com/zh-cn/problem/segment-tree-query/
