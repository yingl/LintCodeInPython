# coding: utf-8

class Solution:
    """
    @param: words: A list of words
    @return: Return how many different rotate words
    """
    def countRotateWords(self, words):
        # Write your code here
        result = {}
        for word in words:
            tp_word = tuple(word)
            if tp_word not in result:
                result[tp_word] = 1
                # 在这里就直接展开方便后面查表
                # 展开后的如果没出现过就置0，
                # 因为我们只统计多少种不同的类型。
                for i in xrange(1, len(word)):
                    shifed_word = Solution._shift(list(word), i)
                    if shifed_word not in result:
                        result[shifed_word] = 0
        ret = 0
        for k, v in result.items():
            ret += v
        return ret
                
    @staticmethod
    def _match(target, word):
        li_word = list(word)
        for i in xrange(len(word)):
            if Solution._shift(li_word, i) == target:
                return True
        return False

    @staticmethod
    def _reverse(word, start, end):
        while start < end:
            word[start], word[end] = word[end], word[start]
            start += 1
            end -= 1
        
    @staticmethod
    def _shift(word, n):
        len_ = len(word)
        Solution._reverse(word, 0, len_ - n - 1)
        Solution._reverse(word, len_ - n, len_ - 1)
        Solution._reverse(word, 0, len_ - 1)
        return tuple(word)
        
# esay: http://lintcode.com/zh-cn/problem/rotate-words/
