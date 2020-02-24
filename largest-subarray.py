class Solution:
    """
    @param A: the array
    @param K: the length 
    @return: the largest subarray
    """
    def largestSubarray(self, A, K):
        # Write your code here.
        ret = 0
        for i in range(1, len(A) - K + 1):
            if cmp_array(A, i, ret, K) > 0:
                ret = i
        return A[ret:ret + K]
        
def cmp_array(A, s_1, s_2, count):
    i = 0
    while i < count:
        if A[s_1 + i] < A[s_2 + i]:
            return -1
        elif A[s_1 + i] > A[s_2 + i]:
            return 1
        else:
            i += 1
    return 0

# easy: https://www.lintcode.com/problem/largest-subarray/
