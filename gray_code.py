# coding: utf-8

class Solution:
    # @param {int} n a number
    # @return {int[]} Gray code
    def grayCode(self, n):
        # Write your code here
        ret = []
        for i in xrange(1 << n):
            ret.append((i >> 1) ^ i)
        return ret

# medium: http://lintcode.com/zh-cn/problem/gray-code/
