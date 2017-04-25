# coding: utf-8

class Solution:
    # @param {string} s A string
    # @return {int} the length of last word
    def lengthOfLastWord(self, s):
        # Write your code here
        ret, i = 0, len(s) - 1
        while i >= 0:
            if s[i] != ' ':
                ret += 1
            elif ret > 0:
                break
            i -= 1
        return ret

# easy: http://lintcode.com/zh-cn/problem/length-of-last-word/
