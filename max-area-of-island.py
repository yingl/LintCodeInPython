def getArea(grid, row, col, area):
    if (row >= 0) and (row < len(grid)) and \
       (col >= 0) and (col < len(grid[0])) and \
       (grid[row][col] == 1):
        grid[row][col] = 0
        area += 1
        area = getArea(grid, row - 1, col, area) # 上
        area = getArea(grid, row + 1, col, area) # 下
        area = getArea(grid, row, col - 1, area) # 左
        area = getArea(grid, row, col + 1, area) # 右
    return area

class Solution:
    """
    @param grid: a 2D array
    @return: the maximum area of an island in the given 2D array
    """
    def maxAreaOfIsland(self, grid):
        # Write your code here
        ret = 0
        if len(grid) == 0:
            return ret
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = getArea(grid, i, j, 0)
                    if area > ret:
                        ret = area
        return ret

# easy: https://www.lintcode.com/problem/max-area-of-island/
