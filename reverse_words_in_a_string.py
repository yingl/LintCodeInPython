# coding: utf-8

class Solution:
    # @param s : A string
    # @return : A string
    def reverseWords(self, s):
        # write your code here
        # 最偷懒的做法，不解释。。。
        words = s.split()
        words.reverse()
        return " ".join(words)

# easy: http://lintcode.com/zh-cn/problem/reverse-words-in-a-string/
