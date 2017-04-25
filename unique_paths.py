# coding: utf-8

class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """
    def uniquePaths(self, m, n):
        if (m < 1) or (n < 1):  
            return 0  
        paths = [[1 for i in range(n)] for j in range(m)]  
        for i in range(1, m):  
            for j in range(1, n):  
                paths[i][j] = paths[i - 1][j] + paths[i][j - 1]  
        return paths[m - 1][n - 1]

# easy: http://lintcode.com/zh-cn/problem/unique-paths/
