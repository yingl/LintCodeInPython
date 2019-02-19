class Solution:
    """
    @param n: a number represent year
    @return: whether year n is a leap year.
    """
    def isLeapYear(self, n):
        # write your code here
        if n % 400 == 0:
            return True
        else:
            return (n % 4 == 0) and (n % 100 != 0)

# easy: https://www.lintcode.com/problem/leap-year
