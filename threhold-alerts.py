class Solution:
    """
    @param n: 
    @param k: 
    @param l: is len
    @param num: //same as problem
    @return: //return long
    """
    def solve(self, n, k, l, num):
        #
        r = 0
        p = 0
        w = num[0 : l]
        s = sum(w)
        if (s / l) > k:
            r += 1
        for i in range(l, len(num)):
            s -= w[p]
            w[p] = num[i]
            s += w[p]
            p += 1
            p %= l
            if (s / l) > k:
                r += 1
        return r

# easy: https://www.lintcode.com/problem/1815/
