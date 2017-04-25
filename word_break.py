# coding: utf-8

class Solution:
    # @param s: A string s
    # @param dict: A dictionary of words dict
    def wordBreak(self, s, dict):
        # write your code here
        if not dict:
            return not s
        len_s = len(s)
        cache = [False] * (len_s + 1)
        cache[0] = True
        max_word_len = max([len(word) for word in dict])  # 字典中最长单词长度
        for i in xrange(1, len_s + 1):
            for j in xrange(1, min(i, max_word_len) + 1):
                if not cache[i - j]:
                    continue
                '''
                判断切分出来部分是否在字典中，这里为代码简单使用数组切片。
                前面必须满足cache[i - j]满足条件。
                '''
                if s[i - j:i] in dict:
                    cache[i] = True
                    break
        return cache[len_s]

# medium: http://lintcode.com/zh-cn/problem/word-break/
