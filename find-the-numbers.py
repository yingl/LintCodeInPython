class Solution:
    """
    @param n: the integer
    @return: the numbers that larger and smaller than `n` 
    """
    def getNumbers(self, n):
        # Write your code here
        if n < 0:
            return []
        if n == 0:
            return [1]
        n0, n1 = 0, 1
        r = [-1, -1]
        while True:
            if n0 < n:
                r[0] = n0
            if n1 > n:
                r[1] = n1
                break
            _n = n0 + n1
            n0 = n1
            n1 = _n
        return r
      
# medium: https://www.lintcode.com/problem/1610/
