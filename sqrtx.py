# coding: utf-8

class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        begin, end = 1, x
        sqrt = (begin + end) / 2
        while True:
            square = sqrt * sqrt
            if square > x:
                end = sqrt
                sqrt = int((begin + end) / 2)
            elif square == x:
                return sqrt
            else:
                begin = sqrt
                sqrt = int((begin + end) / 2)
                if sqrt == begin:
                    return sqrt

# easy: http://lintcode.com/zh-cn/problem/sqrtx/
