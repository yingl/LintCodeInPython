# coding: utf-8

class Solution: 
    # @param S, T: Two string.
    # @return: Count the number of distinct subsequences
    def numDistinct(self, S, T):
        # write your code here
        '''
        根据题目提供的例子，建一张二维表：
            r a b b b i t (S)
        r 0 1 1 1 1 1 1 1   
        a 0 0 1 1 1 1 1 1
        b 0 0 0 1 2 3 3 3
        b 0 0 0 0 1 3 3 3 ＃ 关键在第一个3
        i 0 0 0 0 0 0 3 3
        t 0 0 0 0 0 0 0 3
        (T)
        dp[i][j] = dp[i][j - 1] + (T[i - 1] == S[j - 1] ? dp[i - 1][j - 1] : 0)
        '''
        rows = len(T) + 1
        cols = len(S) + 1
        caches = [[0] * cols for i in xrange(rows)]
        caches[0] = [1] * cols
        for i in xrange(1, rows):
            for j in xrange(1, cols):
                caches[i][j] = caches[i][j - 1]
                if T[i - 1] == S[j - 1]:
                    caches[i][j] += caches[i - 1][j - 1]
        return caches[-1][-1]

# medium: http://lintcode.com/zh-cn/problem/distinct-subsequences/
