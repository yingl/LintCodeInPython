# coding: utf-8

class Solution:
    # @param {string} s Roman representation
    # @return {int} an integer
    def romanToInt(self, s):
        # Write your code here
        '''
        罗马数字的特点是个十百千位的代表数字不一样。
        1 - 10：I, II, III, IV, V, VI, VII, VIII, IX, X
        10 - 100：X, XX, XXX, XL, L, LX, LXX, LXXX,XC, C
        ...
        '''
        ret = 0
        i = 0
        while i < len(s):
            ch = s[i]
            if ch == 'M': # 千位，题目限制小于等于3999
                mul = 1000
                one, five, ten = 'M', '?', '?'
            elif (ch == 'C') or (ch == 'D'): # 百位
                mul = 100
                one, five, ten = 'C', 'D', 'M'
            elif (ch == 'X') or (ch == 'L'): # 十位
                mul = 10
                one, five, ten = 'X', 'L', 'C'
            else: # 个位
                mul = 1
                one, five, ten = 'I', 'V', 'X'
            if ch == one:
                tmp = 1
                j = i + 1
                while (j < len(s)) and (s[j] == one): # 处理连续的1
                    tmp += 1
                    j += 1
                if (j < len(s)) and (s[j] == five):   # 4
                    ret += 4 * mul
                    j += 1
                elif (j < len(s)) and (s[j] == ten):  # 9
                    ret += 9 * mul
                    j += 1
                else:
                    ret += tmp * mul  # 123
            elif ch == five:
                tmp = 5
                j = i + 1
                while (j < len(s)) and (s[j] == one):
                    tmp += 1
                    j += 1
                ret += tmp * mul  # 5678
            i = j
        return ret

# medium: http://lintcode.com/zh-cn/problem/roman-to-integer/
