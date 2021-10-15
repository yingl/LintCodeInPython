class Solution:
    """
    @param A: an array
    @param B: an array
    @return: dot product of two array
    """
    def dotProduct(self, A, B):
        # Write your code here
        if (len(A) != len(B)) or (len(A) == 0):
            return -1
        r = 0
        for i in range(len(A)):
            r += A[i] * B[i]
        return r

# easy: https://www.lintcode.com/problem/1480/
