class Solution:
    """
    @param: k: An integer
    @return: all amicable pairs
    """
    def amicablePair(self, k):
        # write your code here
        ret = []
        for i in range(2, k + 1):
            s = self.vsum(i)
            if  (s <= i) or (s > (k + 1)):
                continue
            if i == self.vsum(s):
                ret.append([i, s])
        return ret

    def vsum(self, v):
        ret = 1
        i = 2
        while i * i < v:
            if v % i == 0:
                ret += (i + int(v / i))
            i += 1
        if i * i == v:
            ret += i
        return ret

# easy: https://www.lintcode.com/problem/243
