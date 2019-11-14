class Solution:
    """
    @param n: a postive Integer
    @return: if two adjacent bits will always have different values
    """
    def hasAlternatingBits(self, n):
        # Write your code here
        if (n % 2) == 0:
            x = int(n / 2)
        else:
            x = n * 2
        r = x ^ n
        return (r & (r + 1)) == 0
        
# easy: https://www.lintcode.com/problem/binary-number-with-alternating-bits/
