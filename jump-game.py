# coding: utf-8

class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        # write your code here
        '''
        贪心
        1. 如果能到k点，那么一定能到比k小的点。
        2. 如果发现某个比k小的点无法到达，那么k点肯定也无法到达。
        '''
        if A is None:
            return False
        index = len(A) - 1
        for i in xrange(len(A) - 1, -1, -1):
            if i + A[i] >= index:
                index = i
        return index == 0

# medium: http://lintcode.com/zh-cn/problem/jump-game/
