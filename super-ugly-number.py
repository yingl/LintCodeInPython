# coding: utf-8

class Solution:
    # @param {int} n a positive integer
    # @param {int[]} primes the given prime list
    # @return {int} the nth super ugly number
    def nthSuperUglyNumber(self, n, primes):
        # Write your code here
        # 参考ugly_number_ii.py的实现，推广到n个数的情况。
        ret = [1]
        candidates = [1] * len(primes)
        ids = [0] * len(primes)
        _next = 1
        for count in xrange(1, n):
            for i in xrange(len(primes)):
                if _next == candidates[i]:
                  candidates[i] = ret[ids[i]] * primes[i]
                  ids[i] += 1
            _next = min(candidates)
            ret.append(_next)
        return ret[-1]

# medium: http://lintcode.com/zh-cn/problem/super-ugly-number/
