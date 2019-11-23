# coding: utf-8

class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """
    def woodCut(self, L, k):
        # write your code here
        if (not L) or (k == 0):
            return 0
        L.sort()
        low, up = 1, L[-1]
        while low <= up:
            mid = low + (up - low) / 2
            if self.calc(L, mid) >= k:
                low = mid + 1
            else:
                up = mid - 1
        return up

    # 计算根据wood_len，总共可以切几段。
    def calc(self, L, wood_len):
        ret = 0
        for l in L:
            ret += l / wood_len
        return ret

# hard: http://lintcode.com/zh-cn/problem/wood-cut/
