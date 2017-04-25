# coding: utf-8

class Solution:
    # @param {list[list[str]]} board a 2D board containing 'X' and 'O'
    # @return nothing 
    def surroundedRegions(self, board):
        # Write your code here
        if not board:
            return
        rows, cols = len(board), len(board[0])
        for col in xrange(cols):    # 第一行
            self.dfs(board, 0, col)
        if rows > 1:  # 如果大于1行，看左右两列和最下行。
            for row in xrange(1, rows - 1): # 最右列
                self.dfs(board, row, cols - 1)
            for col in xrange(cols):  # 最下行
                self.dfs(board, rows - 1, col)
            if cols > 1:
                for row in xrange(1, rows - 1): # 最左列
                    self.dfs(board, row, 0)
        for row in xrange(rows):  # 遍历标记
            for col in xrange(cols):
                if board[row][col] == 'Z':
                    board[row][col] = 'O'
                elif board[row][col] == 'O':
                    board[row][col] = 'X'

    def dfs(self, board, row, col):
        rows, cols = len(board), len(board[0])
        if board[row][col] != 'O':
            return
        board[row][col] = 'Z'
        if row > 0: # 向上
            self.dfs(board, row - 1, col)
        if row < rows - 1:  # 向下
            self.dfs(board, row + 1, col)
        if col > 0: # 向左
            self.dfs(board, row, col - 1)
        if col < cols - 1:  # 向右
            self.dfs(board, row, col + 1)

# medium: http://lintcode.com/zh-cn/problem/surrounded-regions/
