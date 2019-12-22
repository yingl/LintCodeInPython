class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        # write your code here
        self.cache = [0, 1]
        if n < 2:
            return self.cache[n]
        for i in range(2, n):
            tmp = self.cache[1]
            self.cache[1] += self.cache[0]
            self.cache[0] = tmp
        return self.cache[1]
        
# easy: https://www.lintcode.com/problem/fibonacci-easy/
