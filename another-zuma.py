class Solution:
    """
    @param s: the pearl sequences.
    @param k: every k same pearls together will be removed.
    @return: return the pearls after the game.
    """
    def zumaGaming(self, s, k):
        # write your code here.
        sarr = []
        prev = None
        cnt = 0
        for c in s:
            if c != prev:
                if cnt > 0:
                    sarr.append(prev * cnt)
                prev = c
                cnt = 1
            else:
                cnt += 1
                if cnt == k:
                    prev = None
                    cnt = 0
        if prev and (cnt > 0):
            sarr.append(prev * cnt)
        ns = ''.join(sarr)
        if ns != s:
            return self.zumaGaming(ns, k)
        else:
            return ns
            
# medium: https://www.lintcode.com/problem/another-zuma/
