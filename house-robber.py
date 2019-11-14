# coding: utf-8

class Solution:
    # @param A: a list of non-negative integers.
    # return: an integer
    def houseRobber(self, A):
        # write your code here
        '''
        典型的动态规划，到第i间能抢到的最大值可能为以下两种情况：
        1. 抢了第i - 2间，最大值为到第i - 1的最大值加上第i间的值。
        2. 抢了第i - 1间，那么第i间不能抢，最大值就是到第i - 1间的最大值。
        '''
        if not A:
            return 0
        elif len(A) == 1:
            return A[0]
        elif len(A) == 2:
            return max(A[0], A[1])
        else:
            A[1] = max(A[0], A[1])
            for i in xrange(2, len(A)):
                A[i] = max(A[i] + A[i - 2], A[i - 1])
            return A[-1]

# medium: http://lintcode.com/zh-cn/problem/house-robber/
