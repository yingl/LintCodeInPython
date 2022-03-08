class Solution:
    """
    @param arr: the distance between any two cities
    @return: the minimum distance Alice needs to walk to complete the travel plan
    """
    def travelPlan(self, arr):
        # Write your code here.
        self.r = 1000000
        used = set([0])
        paths = [0]
        self.dfs(arr, paths, used)
        return self.r

    def dfs(self, arr, paths, used):
        n = len(arr)
        if len(paths) == n:
            d = 0
            for i in range(n - 1):
                d += arr[paths[i]][paths[i + 1]]
            d += arr[paths[-1]][0]
            if d < self.r:
                self.r = d
            return self.r
        else:
            for i in range(1, n):
                if i not in used:
                    paths.append(i)
                    used.add(i)
                    self.dfs(arr, paths, used)
                    paths.pop()
                    used.remove(i)
                    
# medium: https://www.lintcode.com/problem/1891/
