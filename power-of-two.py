class Solution:
    """
    @param n: an integer
    @return: if n is a power of two
    """
    def isPowerOfTwo(self, n):
        # Write your code here
        if n == 0:
            return False
        return (n & (n - 1)) == 0

# easy: https://www.lintcode.com/problem/power-of-two/
