# coding: utf-8

class Solution:
    # @param: a matrix of integers
    # @return: a list of integers
    def printZMatrix(self, matrix):
        # write your code here
        ret = []
        if matrix:
            rows, cols = len(matrix), len(matrix[0])
            i, count = 1, rows * cols
            row, col = 0, 0
            ret.append(matrix[0][0])
            while i < count:
                if col < (cols - 1):    # 向右
                    col += 1
                    ret.append(matrix[row][col])
                elif row < (rows - 1):  # 不能向右就向下
                    row += 1
                    ret.append(matrix[row][col])
                i += 1
                while (i < count) and (row < (rows - 1)) and (col > 0): # 左下
                    row += 1
                    col -= 1
                    ret.append(matrix[row][col])
                    i += 1
                if (i < count) and (row < (rows - 1)):  # 向下
                    row += 1
                    ret.append(matrix[row][col])
                elif (i < count) and (col < (cols - 1)):    # 向右
                    col += 1
                    ret.append(matrix[row][col])
                    i += 1
                while (i < count) and (row > 0) and (col < (cols - 1)): # 左上
                    row -= 1
                    col += 1
                    ret.append(matrix[row][col])
                    i += 1
        return ret

# easy: http://lintcode.com/zh-cn/problem/matrix-zigzag-traversal/
