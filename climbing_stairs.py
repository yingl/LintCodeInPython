# coding: utf-8

class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if (n == 0) or (n == 1):
            return 1
        if n == 2:
            return 2
        f_1 = 1
        f_2 = 2
        for i in xrange(3, n + 1):
            ret = f_1 + f_2
            f_1 = f_2
            f_2 = ret
        return ret

# easy: http://lintcode.com/problem/climbing-stairs
