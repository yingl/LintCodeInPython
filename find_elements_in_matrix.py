# coding: utf-8

class Solution:
    """
    @param Matrix: the input
    @return: the element which appears every row
    """
    def FindElements(self, Matrix):
        # write your code here
        di = {}
        for row in Matrix:
            rc = {}
            for i in row:
                rc[i] = 1
            for k in rc.keys():
                if k in di:
                    di[k] += 1
                else:
                    di[k] = 1
        for k, v in di.items():
            if v == len(Matrix):
                return k

# easy: http://lintcode.com/zh-cn/problem/find-elements-in-matrix/
