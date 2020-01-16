class Solution:
    """
    @param n: the given number
    @return: Sum of elements in subsets
    """
    def subSum(self, n):
        # write your code here
        if n == 1:
            return 1
        return (1 << (n - 2)) * (1 + n) * n

# easy: https://www.lintcode.com/problem/sum-of-all-subsets/
