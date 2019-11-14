# coding: utf-8

class Solution:
    """
    @param a, b, n: 32bit integers
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        if n == 0:
            return 1 % b
        if 1 == n:
            return a % b
        x = self.fastPower(a, b, n / 2)
        if n % 2 == 1:
            return (((x * x) % b) * a) % b
        else:
            return (x * x) % b

# medium: http://lintcode.com/zh-cn/problem/fast-power/
