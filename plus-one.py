# coding: utf-8

class Solution:
    # @param {int[]} digits a number represented as an array of digits
    # @return {int[]} the result
    def plusOne(self, digits):
        # Write your code here
        number = 0
        for i in xrange(0, len(digits)):
            number = number * 10 + digits[i]
        number += 1
        ret = []
        while number > 0:
            ret.append(number % 10)
            number /= 10
        ret.reverse()
        return ret

# easy: http://lintcode.com/zh-cn/problem/plus-one/
