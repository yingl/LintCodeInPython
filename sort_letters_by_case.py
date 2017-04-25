# coding: utf-8

class Solution:
    """
    @param chars: The letters array you should sort.
    """
    def sortLetters(self, chars):
        # write your code here
        i, j = 0, len(chars) - 1
        while i < j:
            while (i < len(chars)) and ((chars[i] < 'A') or (chars[i] > 'Z')):
                i += 1
            while (j >= 0) and ((chars[j] < 'a') or (chars[j] > 'z')):
                j -= 1
            if (i < j):
                chars[i], chars[j] = chars[j], chars[i]
                i += 1
                j -= 1

# medium: http://lintcode.com/zh-cn/problem/sort-letters-by-case/
