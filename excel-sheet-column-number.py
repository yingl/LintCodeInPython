class Solution:
    """
    @param s: a string
    @return: return a integer
    """
    def titleToNumber(self, s):
        # write your code here
        ret = 0
        for c in s:
            ret = ret * 26 + (ord(c) - ord('A') + 1)
        return ret

# easy: https://www.lintcode.com/problem/excel-sheet-column-number/
