class Solution:
    """
    @param Stock: Stock information
    @return: return id
    """
    def highestGrowth(self, Stock):
        # Write your code here
        r = '0'
        inc = 0
        for s in Stock:
            _inc = float(s[2]) / float(s[1])
            if _inc > inc:
                inc = _inc
                r = s[0]
            elif _inc == inc:
                if s[0] < r:
                    r = s[0]
        return r

# easy: https://www.lintcode.com/problem/1614/
