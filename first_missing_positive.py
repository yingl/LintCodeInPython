# coding: utf-8

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        # write your code here
        '''
        对于每个大于等于0的数放到对应的位置上，
        返回第一个A[i] != i + 1的数。
        '''
        i = 0
        while i < len(A):
            if (A[i] >= len(A)) or (A[i] < 0):
                i += 1  # 不符合条件的数不管！
            elif A[i] != i + 1: # 对于不在对应位置的数要找到正确的位置
                j = A[i]
                if A[i] != A[j - 1]:
                    A[i], A[j - 1] = A[j - 1], A[i]
                else:
                    i += 1
            else:
                i += 1
        for i in xrange(0, len(A)):
            if A[i] != (i + 1):
                return i + 1
        return len(A) + 1

# medium: http://lintcode.com/zh-cn/problem/first-missing-positive/
