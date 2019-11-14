# coding: utf-8

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        # write your code here
        for row in xrange(0, len(board)):
            for col in xrange(0, len(board[0])):
                if self.dfs(board, word, row, col, 0):
                    return True
        return False

    def dfs(self, board, word, row, col, index):
        if index == len(word):
            return True
        rows = len(board)
        cols = len(board[0])
        if (row < 0) or (col < 0) or (row >= rows) or (col >= cols):
            return False
        ch = word[index]
        result = False
        if board[row][col] == ch:
            # 标记当前元素，然后深度优先递归搜索。
            board[row][col] = '*'
            result = self.dfs(board, word, row + 1, col, index + 1) or \
                self.dfs(board, word, row - 1, col, index + 1) or \
                self.dfs(board, word, row, col + 1, index + 1) or \
                self.dfs(board, word, row, col - 1, index + 1)
            if result:
                return result
            else:
                board[row][col] = ch
        else:
            return False

# medium: http://lintcode.com/zh-cn/problem/word-search/
