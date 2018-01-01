# coding: utf-8

class Solution:
    """
    @param: : a given string
    @param: : another given string
    @return: An array of missing string
    """

    def missingString(self, str1, str2):
        # Write your code here
        li_1 = str1.split(' ')
        li_2 = str2.split(' ')
        di = {}
        for word in li_2:
            if word not in di:
                di[word] = True
        ret = []
        for word in li_1:
            if word not in di:
                ret.append(word)
        return ret

# easy: http://lintcode.com/zh-cn/problem/missing-string/
