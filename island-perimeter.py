class Solution:
    """
    @param grid: a 2D array
    @return: the perimeter of the island
    """
    def islandPerimeter(self, grid):
        # Write your code here
        ret = 0
        if len(grid) > 0:
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] != 0:
                        ret += 4 # 周长最大为4
                        # 左边有陆地，减2.两块陆地各减1。
                        if (i > 0) and (grid[i - 1][j] == 1):
                            ret -= 2
                        # 上边有陆地，减2.两块陆地各减1。
                        if (j > 0) and (grid[i][j - 1] == 1):
                            ret -= 2
                        
        return ret
        
# easy: https://www.lintcode.com/problem/island-perimeter/
