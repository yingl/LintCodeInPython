class Solution:
    """
    @param n: An integer
    @return: The sum of a and b
    """
    def dropEggs(self, n):
        # write your code here
        r = 0
        while True:
            s = (1 + r) * r / 2
            if s >= n:
                break
            r += 1
        return r

# easy: https://www.lintcode.com/problem/254/
