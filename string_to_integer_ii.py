# coding: utf-8

class Solution:
    # @param str: a string
    # @return an integer
    def atoi(self, str):
        # write your code here
        int_max = 2147483647
        int_min = -2147483648
        sum = 0
        i = 0
        str = str.strip()
        if not str:
            return 0
        sign = 1
        i = 0
        if str[0] == '-':
            sign = -1
            i = 1
        elif str[0] == '+':
            i = 1
        while i < len(str):
            if not str[i].isdigit():
                break
            digit = int(str[i])
            if int_max / 10 > sum:
                sum *= 10
            else:
                return int_max if sign > 0 else int_min
            if int_max - digit >= sum:
                sum += digit
            else:
                return int_max if sign > 0 else int_min
            i += 1
        return sign * sum

# hard: http://lintcode.com/zh-cn/problem/string-to-integer-ii/
