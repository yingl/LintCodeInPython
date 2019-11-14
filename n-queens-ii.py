# coding: utf-8

class Solution:
    """
    Calculate the total number of distinct N-Queen solutions.
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    def totalNQueens(self, n):
        # write your code here
        self.ret = 0
        self.limit = n
        self.solveNQueens(0, [])
        return self.ret

    def solveNQueens(self, row, queens):
        if row == self.limit:
            self.ret += 1
        else:
            for col in xrange(self.limit):
                if self.check(queens, row, col):
                    queens.append([row, col])
                    self.solveNQueens(row + 1, queens) # 搜索下一行
                    queens.pop()

    def check(self, queens, row, col):
        for queen in queens:
            if (col == queen[1]) or (abs(row - queen[0]) == abs(col - queen[1])):
                return False
        return True

# medium: http://lintcode.com/zh-cn/problem/n-queens-ii/
