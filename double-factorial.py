class Solution:
    """
    @param n: the given number
    @return:  the double factorial of the number
    """
    def doubleFactorial(self, n):
        # Write your code here
        r = 1
        while n > 0:
            r *= n
            n -= 2
        return r
      
# easy: https://www.lintcode.com/problem/771/
