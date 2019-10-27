class Solution:
    """
    @param n: an unsigned integer
    @return: the number of â1' bits
    """
    def hammingWeight(self, n):
        # write your code here
        ret = 0
        while n >= 2:
            if n % 2 != 0:
                ret += 1
            n = int(n / 2)
        return ret + n
        
# easy: https://www.lintcode.com/problem/number-of-1-bits/
