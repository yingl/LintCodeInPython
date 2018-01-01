# coding: utf-8

class Solution:
    """
    @param: s: a string
    @return: it's index
    """
    def firstUniqChar(self, s):
        # write your code here
        di = {}
        for i in range(len(s)):
            c = s[i]
            if c in di:
                di[c] = -1
            else:
                di[c] = i
        ret = len(s)
        for k, v in di.items():
            if (v != -1) and (v < ret):
                ret = v
        if ret == len(s):
            ret = -1
        return ret

# easy: http://lintcode.com/zh-cn/problem/first-position-unique-character/
