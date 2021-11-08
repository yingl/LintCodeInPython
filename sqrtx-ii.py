class Solution:
    """
    @param x: a double
    @return: the square root of x
    """
    def sqrt(self, x):
        # write your code here
        i, j = 0, x
        if x < 1:
            j = 1
        while True:
            m = (i + j) / 2
            m2 = m * m
            if abs(m2 - x) < 0.00000000000001:
                return m
            elif m2 > x:
                j = m
            else:
                i = m
        return -1 
      
# medium: https://www.lintcode.com/problem/586
