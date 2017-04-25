# coding: utf-8

class Solution:
    # @param {int[][]} matrix an integer matrix
    # @return {int[][]} the coordinate of the left-up and right-down number
    def submatrixSum(self, matrix):
        # Write your code here
        '''
        O(n ^ 4)的做法太多了，就不多讨论了。
        1. 原始矩阵如下：
          [1,  5,  7]
          [3,  7, -8]
          [4, -8,  9]
        2. 构造扩展矩阵，令s[i][j]为m[0][0]到m[i - 1][j - 1]的子矩阵和。(闭区间)
          [0,  0,  0,  0]
          [0,  1,  6, 13]
          [0,  4, 16, 15]
          [0,  8, 12, 20]
        3. i2 >= i1, s[i2][k] - s[i1][k]的差等于m[i1][0]到m[i2 - 1][k - 1]的子矩阵的和。(闭区间)
           以s[2][2] - s[1][2] = 16 - 6 = 10。m[1][0]到m[2][1]
        4. 继续步骤3，如果s[i2][j] - s[i1][j]等于s[i2][k] - s[i1][k]，
           那么说明m[i1][k]到m[i2 - 1][j - 1]的子矩阵和为0
        '''
        rows = len(matrix)
        cols = len(matrix[0])
        sums = [[0] * (cols + 1) for i in xrange(rows + 1)]
        for i in xrange(rows):
            for j in xrange(cols):
              sums[i + 1][j + 1] = matrix[i][j] + sums[i + 1][j] + sums[i][j + 1] - sums[i][j]
        ret = [[None, None], [None, None]]
        for i in xrange(rows):
            for j in xrange(i + 1, rows + 1):
                cache = {}
                for k in xrange(cols + 1):
                    sub_sum = sums[j][k] - sums[i][k]
                    if sub_sum in cache:
                        ret[0][0] = i
                        ret[0][1] = cache[sub_sum]
                        ret[1][0] = j - 1
                        ret[1][1] = k - 1
                        return ret
                    cache[sub_sum] = k
        return ret

# medium: http://lintcode.com/zh-cn/problem/submatrix-sum/
