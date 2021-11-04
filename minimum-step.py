class Solution:
    """
    @param colors: the colors of grids
    @return: return the minimum step from position 0 to position n - 1
    """
    def minimumStep(self, colors):
        # write your code here
        ret = 0
        n = len(colors)
        visited = set([])
        points = [set([0]), set()]
        curr, _next = 0, 1
        cmap = {}
        for i in range(n):
            c = colors[i]
            if c not in cmap:
                cmap[c] = set()
            cmap[c].add(i)
        while points[curr]:
            for i in points[curr]:
                if i not in visited:
                    if i == n - 1:
                        return ret
                    if ((i - 1) > 0) and ((i - 1) not in visited):
                        points[_next].add(i - 1)
                    if ((i + 1) < n) and ((i + 1) not in visited):
                        points[_next].add(i + 1)
                    for j in cmap[colors[i]]:
                        if (j != i) and (j not in visited):
                            points[_next].add(j)
                    cmap[colors[i]].clear() # Clear this color! Important!!!
                    visited.add(i)
            points[curr].clear()
            curr, _next = _next, curr
            ret += 1
        return ret
        
# medium: https://www.lintcode.com/problem/1832
