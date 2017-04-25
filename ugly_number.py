# coding: utf-8

class Solution:
    # @param {int} num an integer
    # @return {boolean} true if num is an ugly number or false
    def isUgly(self, num):
        # Write your code here
        if (num <= 0):
            return False
        if (num == 1) or (num == 2) or \
                (num == 3) or (num == 5):
            return True
        else:
            if (num % 5 == 0):
                return self.isUgly(num / 5)
            elif (num % 3 == 0):
                return self.isUgly(num / 3)
            elif (num % 2 == 0):
                return self.isUgly(num / 2)
            else:
                return False

# easy: http://lintcode.com/zh-cn/problem/ugly-number/
