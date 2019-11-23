# coding: utf-8

class Solution:
    # @param {string} s A string
    # @return {boolean} Whether the string is a valid palindrome
    def isPalindrome(self, s):
        # Write your code here
        i, j = 0, len(s) - 1
        while i < j:
            if not (s[i].isalpha() or s[i].isnumeric()):
                i += 1
            elif not (s[j].isalpha() or s[j].isnumeric()):
                j -= 1
            else:
                if s[i].lower() != s[j].lower():
                    return False
                else:
                    i += 1
                    j -= 1
        return True

# easy: http://lintcode.com/zh-cn/problem/valid-palindrome/
