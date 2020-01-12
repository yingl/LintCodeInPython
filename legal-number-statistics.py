class Solution:
    """
    @param a: the array a
    @param L: the integer L
    @param R: the integer R
    @return: Return the number of legal integers
    """
    def getNum(self, a, L, R):
        # Write your code here
        ret = 0
        for i in a:
            if (i >= L) and (i <= R):
                ret += 1
        return ret
        
# easy: https://www.lintcode.com/problem/legal-number-statistics/
