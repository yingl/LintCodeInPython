# coding: utf-8

class Solution:
    # @param {int} n The integer
    # @return {string} Roman representation
    def intToRoman(self, n):
        # Write your code here
        digits = []
        while n > 0:  # 罗马数字没有0
            digits.append(n % 10)
            n /= 10
        ret = ''
        for i in xrange(len(digits) - 1, -1, -1):
            num = digits[i]
            if (num > 0) and (num <= 3):
                if i == 0:  # 个位
                    ret += 'I' * num
                elif i == 1:  # 十位
                    ret += 'X' * num
                elif i == 2:  # 百位
                    ret += 'C' * num
                else: # 千位
                    ret += 'M' * num
            elif num == 4:
                if i == 0:  # 个位
                    ret += 'IV'
                elif i == 1:  # 十位
                    ret += 'XL'
                else: # 百位
                    ret += 'CD'
            elif num == 5:
                if i == 0:  # 个位
                    ret += 'V'
                elif i == 1:  # 十位
                    ret += 'L'
                else: # 百位
                    ret += 'D'
            elif (num >= 6) and (num <= 8):
                if i == 0:  # 个位
                    ret += 'V' + 'I' * (num - 5)
                elif i == 1:  # 十位
                    ret += 'L' + 'X' * (num - 5)
                else: # 百位
                    ret += 'D' + 'C' * (num - 5)
            elif num == 9:
                if i == 0:  # 个位
                    ret += 'IX'
                elif i == 1:  # 十位
                    ret += 'XC'
                else: # 百位
                    ret += 'CM'
        return ret

# medium: http://lintcode.com/zh-cn/problem/integer-to-roman/
