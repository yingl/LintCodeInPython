# coding: utf-8

class Solution:
    # @param {int} num a non-negative integer
    # @return {int} one digit
    def addDigits(self, num):
        # Write your code here
        if num > 9:
            new_num = 0
            while num > 0:
                new_num += num % 10
                num /= 10
            num = self.addDigits(new_num)
        return num
        
# easy: http://lintcode.com/zh-cn/problem/add-digits/
