# coding: utf-8

class Solution:
    # @param {int} n an integer
    # @return {boolean} true if this is a happy number or false
    def isHappy(self, n):
        # Write your code here
        ret = {}
        while True:
            digits = []
            while n > 0:
                digits.append(n % 10)
                n /= 10
            n = 0
            for d in digits:
                n += d * d
            if n == 1:
                return True
            if n in ret:
                return False
            else:
                ret[n] = True

# easy: http://lintcode.com/problem/happy-number
