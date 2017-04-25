# coding: utf-8

class Solution: 
    # @param start, end: Denote an segment / interval
    # @return: The root of Segment Tree
    def build(self, start, end):
        # write your code here
        if start > end:
            return None
        ret = SegmentTreeNode(start, end)
        if start < end:
            ret.left = self.build(start, (start + end) / 2)
            ret.right = self.build((start + end) / 2 + 1, end)
        return ret

# medium: http://lintcode.com/zh-cn/problem/segment-tree-build/
