# coding: utf-8

class Solution:
    # @param s: a string
    # @return: an integer
    def lengthOfLongestSubstring(self, s):
        # write your code here
        ret = 0
        for i in xrange(len(s)):
            char_map = {} # 记录某个字母是否出现
            len_of_substr = 0
            for j in xrange(i, len(s)):
                if s[j] not in char_map:
                    char_map[s[j]] = True
                    len_of_substr += 1
                else:
                    break
            if len_of_substr > ret:
                ret = len_of_substr
        return ret

# medium: http://lintcode.com/zh-cn/problem/longest-substring-without-repeating-characters/
