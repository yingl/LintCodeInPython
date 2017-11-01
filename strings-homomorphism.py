# coding: utf-8

class Solution:
    """
    @param: s: a string
    @param: t: a string
    @return: true if the characters in s can be replaced to get t or false
    """
    def isIsomorphic(self, s, t):
        # write your code here
        sp = self.buildPattern(s)
        tp = self.buildPattern(t)
        return sp == tp
        
    def buildPattern(self, s):
        i = 0
        d = {}
        p = []
        for c in s:
            if c not in d:
                d[c] = i
                i += 1
            p.append(d[c])
        return p

# easy: http://www.lintcode.com/zh-cn/problem/strings-homomorphism/
