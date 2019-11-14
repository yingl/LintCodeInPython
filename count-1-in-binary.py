# coding: utf-8

class Solution:
    # @param num: an integer
    # @return: an integer, the number of ones in num
    def countOnes(self, num):
        # write your code here
        ret = 0
        num &= 0xffffffff
        while num != 0:
            if num & 1:
                ret += 1
            num >>= 1
        return ret

# easy: http://lintcode.com/problem/count-1-in-binary
