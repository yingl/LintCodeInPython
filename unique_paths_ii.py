# coding: utf-8

class Solution:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        paths = [[1 for i in xrange(cols)] for j in xrange(rows)]
        for i in xrange(rows):
            for j in xrange(cols):
                if obstacleGrid[i][j] == 1:
                    paths[i][j] = 0
                else:
                    if (i >= 1) and (j < 1):
                        paths[i][j] = paths[i - 1][j]
                    elif (i < 1) and (j >= 1):
                        paths[i][j] = paths[i][j - 1]
                    elif (i >= 1) and (j >= 1):
                        paths[i][j] = paths[i - 1][j] + paths[i][j - 1]
        return paths[rows - 1][cols - 1]

# easy: http://lintcode.com/zh-cn/problem/unique-paths-ii/
