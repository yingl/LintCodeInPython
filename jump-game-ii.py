# coding: utf-8

class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        # write your code here
        '''
        这题比想象的要难，Google之后才找到一个纯线性的解法。先想明白下面2点：
        1. 从0出发，只需要1步就能覆盖A[1]到A[A[0]]，不可能更少
        2. 那么1 <= i <= A[0]能到达的最远点i + A[i]的步数不可能多余2步。
        '''
        if len(A) >= 2:
            i, steps = 1, 1
            curr_range = A[0] # 当前步数覆盖的最远距离
            next_range = A[0]  # curr_range内下一步能到达的最远距离
            while i <= min(len(A), curr_range):
                next_range = max(next_range, A[i] + i)
                if i == len(A) - 1:
                    return steps
                if i == curr_range: # 到curr_range后面的点必需加1步
                    curr_range = next_range
                    steps += 1
                i += 1
        return 0

    '''
    最直观的动态规划算法，大数据会超时。
        ret = [2147483647] * len(A)
        ret[0] = 0
        for i in xrange(len(A)):
            for j in xrange(A[i]):
                if (i + (j + 1)) < len(A):
                    ret[i + j + 1] = min(ret[j], ret[i] + 1)
        return ret[-1]
    '''

# medium: http://lintcode.com/zh-cn/problem/jump-game-ii/
