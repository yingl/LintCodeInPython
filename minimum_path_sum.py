# coding: utf-8

class Solution:
    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        rows, cols = len(grid), len(grid[0])
        self.min_paths = [[-1] * cols for row in xrange(rows)]
        self.min_paths[0][0] = grid[0][0]
        return self.dfs(grid, rows - 1, cols - 1)
        
    def dfs(self, grid, row, col):
        if self.min_paths[row][col] >= 0:
            return self.min_paths[row][col]
        if (row >= 1) and (col >= 1):
            dist = grid[row][col] + min(self.dfs(grid, row - 1, col), self.dfs(grid, row, col - 1))
        elif row >= 1:
            dist = grid[row][col] + self.dfs(grid, row - 1, col)
        elif col >= 1:
            dist = grid[row][col] + self.dfs(grid, row, col - 1)
        self.min_paths[row][col] = dist
        return dist

# easy: http://lintcode.com/zh-cn/problem/minimum-path-sum/    
