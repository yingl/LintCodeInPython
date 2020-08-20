class Solution:
    """
    @param A: an integer array
    @return: return maxium contiguous non-negative subarray sum
    """
    def maxNonNegativeSubArray(self, A):
        # write your code here
        ret = -1
        s = 0
        for i in A:
            if i >= 0:
                s += i
                if s > ret:
                    ret = s
            else:
                s = 0
        return ret
        
# easy: https://www.lintcode.com/problem/maximum-non-negative-subarray/
