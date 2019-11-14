# coding: utf-8

class Solution:
    #param matrix: a matrix of 0 and 1
    #return: an integer
    def maxSquare(self, matrix):
        # write your code here
        '''
        i - 1, j - 1, i - 1, j
        i, j - 1,     i, j
        [i, j]所属正方形的边长由[i - 1, j - 1], [i - 1, j]和[i, j - 1]共同决定。
        想不通自己画图比划一下。
        '''
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0] * cols for i in xrange(rows)]
        width = 0
        for i in xrange(rows):
            for j in xrange(cols):
                dp[i][j] = matrix[i][j]
                if i and j and dp[i][j]:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                width = max(dp[i][j], width)
        return width * width

# medium: http://lintcode.com/zh-cn/problem/maximal-square/
