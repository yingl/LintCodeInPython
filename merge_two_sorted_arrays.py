# coding: utf-8

class Solution:
    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        # write your code here
        ret = []
        i, j = 0, 0
        while (i < len(A)) and (j < len(B)):
            if A[i] < B[j]:
                ret.append(A[i])
                i += 1
            else:
                ret.append(B[j])
                j += 1
        for k in xrange(i, len(A)):
          ret.append(A[k])
        for k in xrange(j, len(B)):
          ret.append(B[k])
        return ret

# easy: http://lintcode.com/zh-cn/problem/merge-two-sorted-arrays/
