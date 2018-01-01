# coding: utf-8

class Solution:
    """
    @param: : the 1st string
    @param: : the 2nd string
    @return: uncommon characters of given strings
    """

    def concatenetedString(self, s1, s2):
        # write your code here
        di_1, di_2 = {}, {}
        for c in s1:
            if c not in s1:
                s1[c] = True
        for c in s2:
            if c not in s2:
                s2[c] = True
        li = []
        for c in s1:
            if c not in s2:
                li.append(c)
        for c in s2:
            if c not in s1:
                li.append(c)
        return ''.join(li)

# easy: http://lintcode.com/zh-cn/problem/concatenated-string-with-uncommon-characters-of-two-strings/
