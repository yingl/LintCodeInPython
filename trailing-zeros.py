# coding: utf-8

class Solution:
    # @param n a integer
    # @return ans a integer
    def trailingZeros(self, n):
        zeros = 0
        while n > 0:
            zeros += n / 5
            n /= 5
        return zeros

# easy: http://lintcode.com/zh-cn/problem/trailing-zeros/
