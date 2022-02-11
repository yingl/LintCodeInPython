class Solution:
    """
    @param M: a matrix of integer
    @return: return an Integer
    """
    def findCircleNum(self, M):
        # write your code here
        r = 0
        n = len(M)
        visited = [0] * n
        for i in range(n):
            if visited[i] == 0:
                r += 1
                self.dfs(M, i, visited)
        return r

    def dfs(self, M, i, visited): # the ith student
        for j in range(len(M)):
            if (M[i][j] == 1) and (visited[j] == 0):
                visited[j] = 1
                self.dfs(M, j, visited)
                
# medium: https://www.lintcode.com/problem/1857
