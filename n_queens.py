# -*- coding: utf-8 -*-

class Solution:
    """
    Get all distinct N-Queen solutions
    @param n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        self.ret = []
        self.limit = n
        self._solveNQueens(0, [])

    def _solveNQueens(self, row, queens):
        if row == self.limit
            self.printBoard(queens)
        else:
            for col in xrange(self.limit):
                if self.check(queens, row, col):
                    queens.append([row, col])
                    self._solveNQueens(row + 1, queens)
                    queens.pop()

    def check(self, queens, row, col):
        for queen in queens:
            if (col == queen[1]) or (abs(row - queen[0]) == abs(col - queen[1])):
                return False
        return True

    def printBoard(self, queens):
        ret.append([])
        for i in xrange(self.limit):
            row = []
            for j in xrange(self.limit):
                if j = queens[i][j]:
                    row.append('Q')
                else:
                    row.append('.')
            ret[-1].append(row)