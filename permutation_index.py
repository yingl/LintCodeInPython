# coding: utf-8

class Solution:
    # @param {int[]} A an integer array
    # @return {long} a long integer
    def permutationIndex(self, A):
        # Write your code here
        ret = 1
        for i in xrange(0, len(A)):
            fact, rc = 1, 0  # 初始化阶乘与逆序数
            for j in xrange(i + 1, len(A)):
                if A[i] > A[j]:
                    rc += 1
                fact *= (j - i)
            ret += rc * fact
        return ret

# easy: http://lintcode.com/zh-cn/problem/permutation-index/
