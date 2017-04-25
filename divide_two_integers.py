# coding: utf-8

class Solution:
    # @param {int} dividend the dividend
    # @param {int} divisor the divisor
    # @return {int} the result
    def divide(self, dividend, divisor):
        # Write your code here
        if (dividend == -2147483648) and (divisor == -1): # 极端特殊情况
            return 2147483647
        ret = 0
        neg = False
        if (dividend < 0) and (divisor < 0):
            dividend = -dividend
            divisor = -divisor
        elif dividend < 0:
            dividend = -dividend
            neg = True  # 返回值取负号
        elif divisor < 0:
            divisor = -divisor
            neg = True  # 返回值取负号
        if dividend < divisor:
            return ret
        product = divisor
        while product <= dividend:
            if ret == 0:
                ret = 1
            else:
                ret <<= 1 # 乘2
            product <<= 1 # 乘2
        product >>= 1 # 除2
        ret += self.divide(dividend - product, divisor)
        return ret if not neg else -ret

# medium: http://lintcode.com/zh-cn/problem/divide-two-integers/
