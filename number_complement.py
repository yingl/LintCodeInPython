class Solution:
    """
    @param num: an integer
    @return: the complement number
    """
    def findComplement(self, num):
        # Write your code here
        i = 1
        while i <= num:
            i *= 2
        if i == num:
            return i - 1
        else:
            return i -1 - num

# easy: https://www.lintcode.com/problem/number-complement/
