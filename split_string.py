# coding: utf-8

class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        result = []
        Solution._split(s, 0, [], result)
        return result
    
    @staticmethod
    def _split(s, start, tmp, result):
        if start >= len(s):
            result.append(tmp)
            return
        tmp_ = tmp[:]
        tmp_.append(s[start]) # 追加一个字符
        Solution._split(s, start + 1, tmp_, result)
        if start + 2 <= len(s):
            tmp.append(s[start:start + 2]) # 追加两个字符
            Solution._split(s, start + 2, tmp, result)

# easy: http://lintcode.com/zh-cn/problem/split-string/
