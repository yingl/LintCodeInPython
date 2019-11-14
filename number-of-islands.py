# coding: utf-8

class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        # Write your code here
        ret = 0
        if grid:
            for row in xrange(len(grid)):
                for col in xrange(len(grid[0])):
                    if grid[row][col] == 1:
                        ret += 1
                        self.mark(grid, row, col)
        return ret
        
    def mark(self, grid, row, col):
        if grid[row][col] == 1:
            grid[row][col] = -1
            if row > 0: #up
                self.mark(grid, row - 1, col)
            if row < len(grid) - 1: # down
                self.mark(grid, row + 1, col)
            if col > 0: # left
                self.mark(grid, row, col - 1)
            if col < len(grid[0]) - 1:  # right
                self.mark(grid, row, col + 1)

# easy: http://lintcode.com/zh-cn/problem/number-of-islands/
