# coding: utf-8

class Solution:
    # @param {int[][]} matrix a matrix of m x n elements
    # @return {int[]} an integer array
    def spiralOrder(self, matrix):
        # Write your code here
        ret = []
        rows = len(matrix)
        if rows == 0:
            return ret
        columns = len(matrix[0])
        i, j = 0, 0 # 方阵的左上角坐标
        while (rows > 0) and (columns > 0):
            for k in xrange(j, j + columns):  # 第一行
                ret.append(matrix[i][k])
            if rows > 1:  # 行数大于1
                for k in xrange(i + 1, i + rows): # 最右列
                    ret.append(matrix[k][j + columns - 1])
                if columns > 1: # 列数大于1
                    for k in xrange(j + columns - 2, j - 1, -1):  # 最下行
                        ret.append(matrix[i + rows - 1][k])
                    for k in xrange(i + rows - 2, i, -1): # 最左列
                        ret.append(matrix[k][j])
            rows -= 2
            columns -= 2
            i += 1
            j += 1
        return ret

# medium: http://lintcode.com/zh-cn/problem/spiral-matrix/
