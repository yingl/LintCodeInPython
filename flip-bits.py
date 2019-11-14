# coding: utf-8

class Solution:
    """
    @param a, b: Two integer
    return: An integer
    """
    def bitSwapRequired(self, a, b):
        # write your code here
        a ^= b
        if a > 0:
            return self.ones(a)
        else:
            return 32 - self.ones(abs(a) - 1)

    def ones(self, n):
        ret = 0
        n &= 0xffffffff
        while n != 0:
            if n & 1:
                ret += 1
            n >>= 1
        return ret

# easy: http://lintcode.com/problem/flip-bits
