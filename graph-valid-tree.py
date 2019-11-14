# coding: utf-8

class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def validTree(self, n, edges):
        # Write your code here
        # 如果是树，n个点有n - 1条边，遍历后包含所有点。
        if len(edges) != (n - 1):
            return False
        # 重新构造无向树，[m, n] => t[m][n] = t[n][m] = True。
        tree = [[False] * n for i in xrange(n)]
        visited = [False] * n
        for edge in edges:
            tree[edge[0]][edge[1]] = True
            tree[edge[1]][edge[0]] = True
        # 从节点0开始深度遍历，这里顺便解决了输入为"1, []"的情况。
        self.dfs(tree, visited, 0)
        for i in xrange(n):
            if not visited[i]:
                return False
        return True

    def dfs(self, tree, visited, node):
        visited[node] = True
        for i in xrange(len(tree[node])):
            if tree[node][i] and (not visited[i]):
                self.dfs(tree, visited, i)

# medium: http://lintcode.com/zh-cn/problem/graph-valid-tree/
