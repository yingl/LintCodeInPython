# coding: utf-8

class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci(self, n):
        # write your code here
        if (n == 1) or (n == 2):
            return n - 1
        ret = 0
        f_1, f_2 = 0, 1
        for i in range(3, n + 1):
            ret = f_1 + f_2
            f_1 = f_2
            f_2 = ret
        return ret
        
# naive: http://www.lintcode.com/zh-cn/problem/fibonacci/
