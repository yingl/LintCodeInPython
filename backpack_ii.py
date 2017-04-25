# coding: utf-8

class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A & V: Given n items with size A[i] and value V[i]
    # @return: The maximum value
    def backPackII(self, m, A, V):
        # write your code here
        '''
        肯定是动态规划！
        dp[i][j]表示前i个商品在j空间能获得的最大价值。
        1. 如果不放第i个商品：d[i][j] = dp[i - 1][j]
        2. 如果放第i个商品：d[i][j] = dp[i - 1][j] + v[i]
        注意：A是体积，V是价值。
        '''
        ret = [0] * (m + 1)
        for i in xrange(len(A)):
            for j in xrange(m, -1, -1):
                if j >= A[i]: # 有足够的体积容纳第i件商品
                    ret[j] = max(ret[j], ret[j - A[i]] + V[i])
        return ret[-1]

# medium: http://lintcode.com/zh-cn/problem/backpack-ii/
