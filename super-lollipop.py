class Solution:
    """
    @param v1: the speed of GGbond
    @param v2: the speed of SuperQ
    @param s: the speed that lollipop can add
    @param w: the cost of lollipop
    @return: the minimal price
    """
    def getAns(self, v1, v2, s, w):
        # Write your code here
        ret = max(w)
        if v1 > v2:
            return 0
        for i in range(len(s)):
            if (v1 + s[i]) > v2:
                ret = min(w[i], ret)
        return ret

# easy: https://www.lintcode.com/problem/super-lollipop/
