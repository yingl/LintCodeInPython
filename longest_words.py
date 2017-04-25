# coding: utf-8

class Solution:
    # @param dictionary: a list of strings
    # @return: a list of strings
    def longestWords(self, dictionary):
        # write your code here
        ret = []
        max_word_len = 0
        for word in dictionary:
            word_len = len(word)
            if word_len > max_word_len:
                max_word_len = word_len
                ret = []
                ret.append(word)
            elif word_len == max_word_len:
                ret.append(word)
        return ret

# easy: http://lintcode.com/zh-cn/problem/longest-words/
