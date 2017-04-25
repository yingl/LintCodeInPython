# coding: utf-8

class Solution:
    """
    @param matrix: A list of lists of integers
    @return: Nothing
    """
    def rotate(self, matrix):
        # write your code here
        rows = len(matrix)
        '''
        原始矩阵和目标矩阵为
          1 2 3      7 4 1
          4 5 6  =>  8 5 2
          7 8 9      9 6 3
        先对非对角线元素做行列转置，实际只要做上半三角。
          1 4 7
          2 5 8
          3 6 9
        然后左右往当中列互换即可。
        '''
        if rows > 1:
            for i in xrange(rows):
                for j in xrange(i + 1, rows):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            i, j = 0, rows - 1
            while i < j:
                for k in xrange(rows):
                    matrix[k][i], matrix[k][j] = matrix[k][j], matrix[k][i]
                i += 1
                j -= 1
        return matrix

# medium: http://lintcode.com/zh-cn/problem/rotate-image/
