class Solution:
    """
    @param n: a integer
    @return: return a string
    """
    def convertToTitle(self, n):
        # write your code here
        ret = []
        while n != 0:
            i = n % 26
            if i == 0:
                i = 26
            n = int((n - i) / 26)
            ret.append(chr(ord('A') + i - 1))
        return ''.join(ret[::-1])

# easy: https://www.lintcode.com/problem/excel-sheet-column-title/
