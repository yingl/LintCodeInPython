# coding: utf-8

class Solution:
    """
    @param A: Given an integers array A
    @return: An integer array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, A):
        # write your code here
        B = [1] * len(A)
        for i in xrange(0, len(A)):
            for j in xrange(0, len(A)):
                if j != i:
                    B[i] *= A[j]
        return B

# easy: http://lintcode.com/zh-cn/problem/product-of-array-exclude-itself/
