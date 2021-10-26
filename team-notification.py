class Solution:
    """
    @param n: the number of members in team.
    @param groups: the groups.
    @return: return how many members will get notifications.
    """
    def teamNotification(self, n, groups):
        # write your code here.
        u = UnionSearch(n)
        for g in groups:
            if g:
                x = g[0]
                for i in range(1, len(g)):
                    u.union(x, g[i])
        return u.get_count(0)

class UnionSearch:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = [1] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.parent[py] = x
            self.count[px] += self.count[py]

    def get_count(self, x):
        return self.count[self.find(x)]
      
# medium: https://www.lintcode.com/problem/337
