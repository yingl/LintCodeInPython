# coding: utf-8

class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, A):
        # write your code here
        ret = -1
        for i in xrange(len(A)):
            left = A[i - 1] if (i - 1) >= 0 else -2147483648
            right = A[i + 1] if (i + 1) < len(A) else -2147483648
            if A[i] > max(left, right):
                if ret == -1:
                    ret = i
                elif A[i] > A[ret]:
                    ret = i
        return ret

# medium: http://lintcode.com/zh-cn/problem/find-peak-element/
