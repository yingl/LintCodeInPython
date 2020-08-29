class Solution:
    """
    @param A: the array A
    @param B: the array B
    @return: returns an alternate array of arrays A and B.
    """
    def interleavedArray(self, A, B):
        # Interleaved Array
        ret = []
        for i in range(len(A)):
            ret.append(A[i])
            ret.append(B[i])
        return ret

# easy: https://www.lintcode.com/problem/interleaved-array/
