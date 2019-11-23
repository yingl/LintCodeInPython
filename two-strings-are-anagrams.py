# coding: utf-8

class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        # write your code here
        char_map = {}
        for ch in s:
            if ch not in char_map:
                char_map[ch] = 1
            else:
                char_map[ch] += 1
        for ch in t:
            if ch not in char_map:
                return False
            else:
                char_map[ch] -= 1
        for key, value in char_map.items():
            if value != 0:
                return False
        return True

# easy: http://lintcode.com/zh-cn/problem/two-strings-are-anagrams/
