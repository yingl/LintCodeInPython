# coding: utf-8

class Solution:
    """
    @param A: sorted integer array A which has m elements, 
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        i, j, k = m - 1, n - 1, m + n - 1
        while (i >= 0) and (j >= 0):
            if A[i] >= B[j]:
                A[k] = A[i]
                i -= 1
            else:
                A[k] = B[j]
                j -= 1
            k -= 1
        if i < 0:
            for k in xrange(j + 1):
                A[k] = B[k]

# easy: http://lintcode.com/zh-cn/problem/merge-sorted-array/
