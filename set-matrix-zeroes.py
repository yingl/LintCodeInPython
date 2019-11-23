# coding: utf-8

class Solution:
    """
    @param matrix: A list of lists of integers
    @return: Nothing
    """
    def setZeroes(self, matrix):
        # write your code here
        if not matrix:
            return
        rows = len(matrix)
        cols = len(matrix[0])
        # 确定第1行是非有0要处理
        zero_first_row = False
        for col in range(0, cols):
            if matrix[0][col] == 0:
                zero_first_row = True
                break
        # 确定第1列是非有0要处理
        zero_first_col = False
        for row in range(0, rows):
            if matrix[row][0] == 0:
                zero_first_col = True
                break
        # 利用第1行和第1列，标记某行某列需要清零。
        for row in xrange(1, rows):
            for col in xrange(1, cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
        # 根据标记清零。
        for row in xrange(1, rows):
            if matrix[row][0] == 0:
                zero_row(matrix, row, 0, cols)
        for col in xrange(1, cols):
            if matrix[0][col] == 0:
                zero_col(matrix, col, 0, rows)
        # 判断第1行和第1列是否需要清理
        if zero_first_row:
            zero_row(matrix, 0, 0, cols)
        if zero_first_col:
            zero_col(matrix, 0, 0, rows)

def zero_row(matrix, row, left, right):
    while left < right:
        matrix[row][left] = 0
        left += 1

def zero_col(matrix, col, up, low):
    while up < low:
        matrix[up][col] = 0
        up += 1

# medium: http://lintcode.com/zh-cn/problem/set-matrix-zeroes/
