# coding: utf-8

class Solution:
    # @param s: a list of char
    # @param offset: an integer
    # @return: nothing
    def rotateString(self, s, offset):
        # write you code here
        if s:
            shift = offset % len(s)
            if shift > 0:
                '''
                abcdefg, 2 => fgabcde
                ab => ba, cdefg => gfedc
                bagfedc => cdefgab
                '''
                self.reverse(s, 0, len(s) - shift - 1)
                self.reverse(s, len(s) - shift, len(s) - 1)
                s.reverse()

    def reverse(self, s, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

# easy: http://lintcode.com/zh-cn/problem/rotate-string/
