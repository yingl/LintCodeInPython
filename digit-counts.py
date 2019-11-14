# coding: utf-8

class Solution:
    # @param k & n  two integer
    # @return ans a integer
    def digitCounts(self, k, n):
        ret = 0
        for i in xrange(n + 1):
            ret += self.check_k(i, k)
        return ret
        
    def check_k(self, i, k):
        if i == k:
            return 1
        else:
            ret = 0
            while i != 0:
                if (i % 10) == k:
                    ret += 1
                i /= 10
            return ret

# medium: http://lintcode.com/zh-cn/problem/digit-counts/
