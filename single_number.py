# coding: utf-8

class Solution:
    """
    @param A : an integer array
    @return : a integer
    """
    def singleNumber(self, A):
        # write your code here
        ret = 0
        for num in A:
            ret ^= num
        return ret

# easy: http://lintcode.com/zh-cn/problem/single-number/
