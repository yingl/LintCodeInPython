# coding: utf-8

class Solution:
    # @param {int[]} A an array of Integer
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequence(self, A):
        # Write your code here
        len_a = len(A)
        if len_a <= 1:
            return len_a
        sign = 1 if A[0] < A[1] else -1
        i, seq_count, max_seq_count = 1, 1, 0
        while i < len_a:
            if sign > 0:
                if A[i] >= A[i - 1]:
                    seq_count += 1
                else:
                    if seq_count > max_seq_count:
                        max_seq_count = seq_count
                    seq_count = 2
                    sign = -1
            else:
                if A[i] <= A[i - 1]:
                    seq_count += 1
                else:
                    if seq_count > max_seq_count:
                        max_seq_count = seq_count
                    seq_count = 2
                    sign = 1
            i += 1
        return max_seq_count if max_seq_count >= seq_count else seq_count

# easy: http://lintcode.com/zh-cn/problem/longest-increasing-continuous-subsequence/
