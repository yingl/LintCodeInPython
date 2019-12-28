class Solution:
    """
    @param n: an integer
    @return: return an integer
    """
    def reverseBits(self, n):
        # write your code here
        ret = 0
        step = 31
        while n:
            i = n % 2
            ret += i << step
            step -= 1
            n = int((n - i) / 2)
        return ret
        
# easy: https://www.lintcode.com/problem/reverse-bits/
