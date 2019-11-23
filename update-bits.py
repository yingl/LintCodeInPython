# coding: utf-8

class Solution:
    #@param n, m: Two integer
    #@param i, j: Two bit positions
    #return: An integer
    def updateBits(self, n, m, i, j):
        # write your code here
        bits = []
        for k in xrange(32):  # 将n转为二进制bits
            bits.append(n % 2)
            n /= 2
        for k in xrange(i, j + 1):  # 将第i到j位转为m的二进制bits
            bits[k] = m % 2
            m /= 2
        n = 0
        for k in xrange(31):
            if bits[k] == 1:
                n |= (1 << k)
        if bits[31] == 1:  # 负号
            n -= (1 << 31)
        return n

# medium: http://lintcode.com/zh-cn/problem/update-bits/
