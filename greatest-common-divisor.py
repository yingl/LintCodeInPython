class Solution:
    """
    @param a: the given number
    @param b: another number
    @return: the greatest common divisor of two numbers
    """
    def gcd(self, a, b):
        # write your code here
        x = max(a, b)
        y = min(a, b)
        while (x % y) != 0:
            tmp = x % y
            x = y
            y = tmp
        return y

# easy: https://www.lintcode.com/problem/greatest-common-divisor/
