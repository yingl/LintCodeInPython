# coding: utf-8

class Solution:
    # @param {boolean[][]} matrix, a list of lists of boolean
    # @return {int} an integer
    def maximalRectangle(self, matrix):
        # Write your code here
        if not matrix:
            return 0
        ret = 0
        rows, cols = len(matrix), len(matrix[0])
        height = [0] * cols
        left, right = [0] * cols, [cols] * cols
        for i in xrange(rows):
            cur_left, cur_right = 0, cols
            # 更新当前列的高度
            for j in xrange(cols):
                height[j] = (height[j] + 1) if matrix[i][j] else 0
            # 更新列上元素所属矩阵的左边界
            for j in xrange(cols):
                if matrix[i][j]:
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1
            # 更新列上元素所属矩阵的右边界，不减1是方便后面计算宽度。
            for j in xrange(cols - 1, -1, -1):
                if matrix[i][j]:
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = cols
                    cur_right = j
            # 根据左右矩阵的计算方式，max和min函数保证在范围内height[j]有效。
            for j in xrange(cols):
                ret = max(ret, (right[j] - left[j]) * height[j])
        return ret

# hard: http://lintcode.com/zh-cn/problem/maximal-rectangle/
