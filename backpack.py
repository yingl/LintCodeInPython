# coding: utf-8

class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backPack(self, m, A):
        # write your code here
        '''
        动态规划，已m = 10，A = [3, 4, 8, 5]为例：
        1. A[0] = 3, c[10] ... C[3] = 3
        2. A[1] = 4
          - c[10] = max(c[10 - 4] + 4, c[10]) = max(c[6] + 4, c[10]) = 7
          - c[7] = c[8] = c[9] = 7
          - c[6] = max(c[6 - 4] + 4, c[6]) = 4
          - c[4] = c[5] = 4
        c[i]表示大小为i的空间的最大容量，对于大小为k的物品，状态转移方程为：c[i] = max(c[i - k] + k, c[i])
        '''
        capacities = [0] * (m + 1)
        if A:
            for i in xrange(len(A)):
                for j in xrange(m, A[i] - 1, -1):
                    capacities[j] = max(capacities[j - A[i]] + A[i], capacities[j])
        return capacities[-1]

# medium: http://lintcode.com/zh-cn/problem/backpack/
