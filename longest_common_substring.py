# coding: utf-8

class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        # write your code here
        # 如果A[i]等于B[j]，那么子串的长度等于c[i - 1][j - 1] ＋ 1。
        ret = 0
        cache = [[0] * (len(B) + 1) for i in xrange(len(A) + 1)]
        for i in xrange(1, len(A) + 1):
            for j in xrange(1, len(B) + 1):
                cache[i][j] = cache[i - 1][j - 1] + 1 if A[i - 1] == B[j - 1] else 0
                ret = max(cache[i][j], ret)
        return ret

# medium: http://lintcode.com/zh-cn/problem/longest-common-substring/
