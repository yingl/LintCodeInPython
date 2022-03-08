import math
import sys

class Solution:
    """
    @param barracks: the position of barracks
    @return: the minimum of the maximum of the distance
    """
    def fetchSuppliesII(self, barracks):
        # write your code here
        ret, mret = 0, 0
        l, r = sys.maxsize, -1
        for b in barracks:
            if b[0] > r:
                r = b[0]
            if b[0] < l:
                l = b[0]
        for i in range(100):
            mid = l + (r - l) / 2;
            mmid = mid + (r - mid) / 2;
            ret = self.maxDist(mid, barracks)
            mret = self.maxDist(mmid, barracks)
            if(ret > mret):
                l = mid;
            else:
                r = mmid;
        return math.sqrt(ret)

    def maxDist(self, x, barracks):
        r = 0
        for b in barracks:
            d = (x - b[0]) * (x - b[0]) + b[1] * b[1]
            if d > r:
                r = d
        return r
      
# medium: https://www.lintcode.com/problem/1899/
