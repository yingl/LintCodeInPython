# coding: utf-8

class Solution:
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    def reverseInteger(self, n):
        # Write your code here
        plus = (n >= 0) # 判断正负号
        abs_n = abs(n)
        numbers = []
        while abs_n > 0:
            numbers.append(abs_n % 10)
            abs_n /= 10
        ret = 0
        for i in xrange(0, len(numbers)):
            ret = ret * 10 + numbers[i]
        if ret > 0x7fffffff:  # 32位符号数限制
            return 0
        else:
            return ret if plus else -ret

# easy: http://lintcode.com/zh-cn/problem/reverse-integer/
