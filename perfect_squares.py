# coding: utf-8

class Solution:
    # @param {int} n a positive integer
    # @return {int} an integer
    def numSquares(self, n):
        # Write your code here
        # Python效率问题，代码翻译成Java可通过。
        cache = [2147483647] * (n + 1)
        cache[0] = 0
        for i in xrange(n + 1):
            for j in xrange(1, n + 1):
                if (i + j * j) <= n:
                    cache[i + j * j] = min(cache[i + j * j], cache[i] + 1)
                else:
                    break
        return cache[-1]

# medium: http://lintcode.com/zh-cn/problem/perfect-squares/
