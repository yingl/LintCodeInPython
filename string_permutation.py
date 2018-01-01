# coding: utf-8

class Solution:
    """
    @param: A: a string
    @param: B: a string
    @return: a boolean
    """
    def Permutation(self, A, B):
        # write your code here
        di = {}
        for s in A:
            if s not in di:
                di[s] = 1
            else:
                di[s] += 1
        for s in B:
            if s not in di:
                return False
            else:
                di[s] -= 1
        for k, v in di.items():
            if v != 0:
                return False
        return True
        
# esay: http://lintcode.com/zh-cn/problem/string-permutation/
