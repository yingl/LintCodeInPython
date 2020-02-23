class Solution:
    """
    @param g: children's greed factor
    @param s: cookie's size
    @return: the maximum number
    """
    def findContentChildren(self, g, s):
        # Write your code here
        # 贪心，优先分配小饼干。
        ret = 0
        g.sort()
        s.sort()
        i_g, i_s = 0, 0
        while (i_g < len(g)) and (i_s < len(s)):
            if s[i_s] < g[i_g]: # 当前饼干不满足需求
                i_s += 1
            else:
                i_s += 1
                i_g += 1
                ret += 1
        return ret

# easy: https://www.lintcode.com/problem/assign-cookies/
