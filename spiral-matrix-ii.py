# coding: utf-8

class Solution:
    # @param {int} n an integer
    # @return {int[][]} a square matrix
    def generateMatrix(self, n):
        # Write your code here
        ret = [[1 for i in xrange(n)] for i in xrange(n)]
        k = 1   # 初始值
        loop = 0    # 已走过圈数
        while loop <= (n / 2):  # 用小于等于可以覆盖n为奇偶数的情况
            steps = n - loop * 2
            for i in xrange(steps): # 最上面一行
                ret[loop][loop + i] = k
                k += 1
            for i in xrange(steps - 1): # 最右面一列
                ret[loop + 1 + i][n - loop - 1] = k
                k += 1
            for i in xrange(steps - 1): # 最左面一列
                ret[n - loop - 1][n - loop - 2 - i] = k
                k += 1
            for i in xrange(steps - 2): # 最下面一行
                ret[n - loop - 2 - i][loop] = k
                k += 1
            loop += 1
        return ret

# medium: http://lintcode.com/zh-cn/problem/spiral-matrix-ii/
