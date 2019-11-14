# coding: utf-8

class Solution:
    # @param n: An integer.
    # return : A list of integer storing 1 to the largest number with n digits.
    def numbersByRecursion(self, n):
        # write your code here
        self.ret = []
        if n > 0:
            self._numbersByRecursion(1, n)
        return self.ret

    def _numbersByRecursion(self, val, n):
        new_val = val * 10  # 把递归降低到n次
        for i in xrange(val, new_val):
            self.ret.append(i)
        if n == 1:
            return
        self._numbersByRecursion(new_val, n - 1)

# medium: http://lintcode.com/zh-cn/problem/print-numbers-by-recursion/
