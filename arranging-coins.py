class Solution:
    """
    @param n: a non-negative integer
    @return: the total number of full staircase rows that can be formed
    """
    def arrangeCoins(self, n):
        # Write your code here
        i = 1
        while True:
            if n - i > 0:
                n -= i
                i += 1
            elif n - i == 0:
                return i
            else:
                return i - 1

# easy: https://www.lintcode.com/problem/arranging-coins/
