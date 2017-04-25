# coding: utf-8

class Solution:
    # @param {double} x the base number
    # @param {int} n the power number
    # @return {double} the result
    def myPow(self, x, n):
        # Write your code here
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n < 0:
            return 1 / self.myPow(x, -n)
        else:
            k = self.myPow(x, n / 2)
            k2 = k * k
            return k2 if (n % 2 == 0) else (k2 * x)

# medium: http://lintcode.com/zh-cn/problem/powx-n/
