# coding: utf-8

class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: Cosine similarity.
    """
    def cosineSimilarity(self, A, B):
        # write your code here
        sqr_a, sqr_b, sum_a_dot_b = 0, 0, 0
        for i in xrange(len(A)):
            sqr_a += A[i] * A[i]
            sqr_b += B[i] * B[i]
            sum_a_dot_b += A[i] * B[i]
        if sqr_a == 0 or sqr_b == 0:
            return 2.0
        return sum_a_dot_b / math.sqrt(sqr_a * sqr_b)

# easy: http://lintcode.com/zh-cn/problem/cosine-similarity/
