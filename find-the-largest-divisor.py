class Solution:
    """
    @param A: the array.
    @param k: the integer.
    @return: the divisor satisfy the requirement.
    """
    def FindDivisor(self, A, k):
        #
        start, end = 1, max(A)
        mid = -1
        while start < (end - 1):
            mid = int((start + end) / 2)
            if self._test(A, mid, k):
                start = mid
            else:
                end = mid
        return end if self._test(A, end, k) else start
        
    def _test(self, A, i, k):
        s = 0
        for v in A:
            s += math.ceil(v / i)
        return s>= k
        
# medium: https://www.lintcode.com/problem/find-the-largest-divisor/
