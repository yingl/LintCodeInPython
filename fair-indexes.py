class Solution:
    """
    @param A: an array of integers
    @param B: an array of integers
    @return: return a integer indicating the number of fair indexes.
    """
    def CountIndexes(self, A, B):
        # Write your code here.
        r = 0
        l = len(A)
        sa, sb = sum(A), sum(B)
        if sa != sb:
            return 0
        t = int(sa / 2)
        ha, hb = 0, 0
        for i in range(l - 1):
            ha += A[i]
            hb += B[i]
            if (ha == hb) and (ha == t):
                r += 1
        return r
      
# medium: https://www.lintcode.com/problem/1882/
