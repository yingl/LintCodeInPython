class Solution:
    """
    @param n: An integer
    @return: An Integer
    """
    def climbStairs2(self, n):
        # write your code here
        self.cache = [-1] * (n + 1)
        self.cache[0] = 1
        self._climbStairs2(n)
        return self.cache[n]
        
    def _climbStairs2(self, n):
        if n < 0:
            return 0
        if self.cache[n] == -1:
            if n <= 2:
                self.cache[n] = n
            else:
                self.cache[n] = self._climbStairs2(n - 1) + self._climbStairs2(n - 2) + self._climbStairs2(n - 3)
        return self.cache[n]
        
# easy: https://www.lintcode.com/problem/climbing-stairs-ii/
