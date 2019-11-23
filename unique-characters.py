# coding: utf-8

class Solution:
    # @param s: a string
    # @return: a boolean
    def isUnique(self, str):
        # write your code here
        char_map = {}
        for ch in str:
            if ch not in char_map:
                char_map[ch] = True
            else:
                return False
        return True

# easy: http://lintcode.com/zh-cn/problem/unique-characters/
