# coding: utf-8

class Solution: 
    # @oaram A: a list of integer
    # @return: The root of Segment Tree
    def build(self, A):
        # write your code here
        if not A:
            return None
        return self._build(A, 0, len(A) - 1)

    def _build(self, array, start, end):
        if start > end:
            return None
        if start == end:  # 构造叶子节点
            return SegmentTreeNode(start, end, array[start])
        else:
            left = self._build(array, start, (start + end) / 2)
            right = self._build(array, (start + end) / 2 + 1, end)
            node = SegmentTreeNode(start, end, left.max)
            if right: # 如果右节点不会空，更新最大值。
                node.max = max(node.max, right.max)
            node.left, node.right = left, right
            return node

# medium: http://lintcode.com/zh-cn/problem/segment-tree-build-ii/
