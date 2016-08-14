# -*- coding: utf-8 -*-

class Solution:
    """
    @param A, B: Two strings.
    @return: The length of longest common subsequence of A and B.
    """
    def longestCommonSubsequence(self, A, B):
        # write your code here
        self.ret = 0
        self.cache = [[-1] * len(A) for i in xrange(len(B))]  # 缓存，避免重复计算
        self._longestCommonSubsequence(A, B, 0, 0)
        return self.ret

    def _longestCommonSubsequence(self, A, B, start_a, start_b):
        if (start_a >= len(A)) or (start_b >= len(B)):
            return 0
        elif self.cache[start_a][start_b] == -1:
            if A[start_a] != B[start_b]:
                len_a = self._longestCommonSubsequence(A, B, start_a + 1, start_b)
                len_b = self._longestCommonSubsequence(A, B, start_a, start_b + 1)
                self.ret = max(max(len_a, len_b), self.ret) # LCS不要求连续
                self.cache[start_a][start_b] = max(len_a, len_b)
            else:
                _len = self._longestCommonSubsequence(A, B, start_a + 1, start_b + 1)
                self.ret = max(_len + 1, self.ret)
                self.cache[start_a][start_b] = _len + 1
        return self.cache[start_a][start_b]