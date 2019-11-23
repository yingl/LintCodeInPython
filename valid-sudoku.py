# coding: utf-8

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        # 检查行
        for row in xrange(0, 9):
            visited = [False] * 9 # 记录出现过的元素
            for column in xrange(0, 9):
                if not self.check(board, row, column, visited):
                    return False

        # 检查列
        for column in xrange(0, 9):
            visited = [False] * 9
            for row in xrange(0, 9):
                if not self.check(board, row, column, visited):
                    return False

        # 检查3*3小方块
        for block in xrange(0, 9):
            visited = [False] * 9
            for i in xrange(0, 9):
                row = int(block / 3) + int(i / 3)
                column = (block % 3) * 3 + (i % 3)
                if not self.check(board, row, column, visited):
                    return False
        return True

    def check(self, board, row, column, visited):
        ch = board[row][column]
        if ch != '.':
            index = int(ch) - 1
            if not visited[index]:
                visited[index] = True
                return True
            else:
                return False
        return True

# easy: http://lintcode.com/zh-cn/problem/valid-sudoku/
