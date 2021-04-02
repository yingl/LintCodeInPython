class Solution:
    """
    @param grid: a matrix
    @return: Find all points that are strictly larger than their neighbors
    """
    def highpoints(self, grid):
        # write your code here
        rows = len(grid)
        cols = len(grid[0])
        marks = [[-1] * cols for _ in range(rows)]
        for r in range(rows):
          for c in range(cols):
            if marks[r][c] == -1:
              if self.check_and_mark(grid, marks, r, c, r - 1, c): # 上
                continue
              if self.check_and_mark(grid, marks, r, c, r + 1, c): # 下
                continue
              if self.check_and_mark(grid, marks, r, c, r, c - 1): # 左
                continue
              if self.check_and_mark(grid, marks, r, c, r, c + 1): # 右
                continue
              if self.check_and_mark(grid, marks, r, c, r - 1, c - 1): # 左上
                continue
              if self.check_and_mark(grid, marks, r, c, r + 1, c - 1): # 左下
                continue
              if self.check_and_mark(grid, marks, r, c, r - 1, c + 1): # 右上
                continue
              if self.check_and_mark(grid, marks, r, c, r + 1, c + 1): # 右下
                continue
              marks[r][c] = 1
        return marks

    def check_and_mark(self, grid, marks, r1, c1, r2, c2):
        rows = len(grid)
        cols = len(grid[0])
        if ((r2 >= 0) and (r2 < rows)) and ((c2 >= 0) and (c2 < cols)):
          if grid[r1][c1] <= grid[r2][c2]:
            marks[r1][c1] = 0
            return True
        return False
      
# easy: https://www.lintcode.com/problem/look-for-points-that-are-bigger-than-the-surrounding-area/
