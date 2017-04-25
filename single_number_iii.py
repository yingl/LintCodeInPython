# coding: utf-8

class Solution:
    """
    @param A : An integer array
    @return : Two integer
    """
    def singleNumberIII(self, A):
        # write your code here
        A.sort()
        i = 0
        while (i + 1) < len(A):
            if (A[i] ^ A[i + 1]) != 0:
                break
            i += 2
        ret_1 = A[i]
        ret_2 = self.singleNumber(A, i + 1, len(A))
        return ret_1, ret_2
    
    def singleNumber(self, A, start, end):
        ret = 0
        while start < end:
            ret ^= A[start]
            start += 1
        return ret

# medium: http://lintcode.com/zh-cn/problem/single-number-iii/
