# coding: utf-8

class Solution:
    # @param {string} a a number
    # @param {string} b a number
    # @return {string} the result
    def addBinary(self, a, b):
        # Write your code here
        flag = 0
        ret = ''
        a_i, b_i = len(a) - 1, len(b) - 1
        while (a_i >= 0) and (b_i >= 0):
            va, vb = int(a[a_i]), int(b[b_i])
            ret += str((va + vb + flag) % 2)
            flag = (va + vb + flag) / 2
            a_i -= 1
            b_i -= 1
        c_i = -1
        if (a_i >= 0) or (b_i >= 0):
            c = a if a_i >= 0 else b
            c_i = a_i if a_i >= 0 else b_i
        while c_i >= 0:
            ret += str((int(c[c_i]) + flag) % 2)
            flag = (int(c[c_i]) + flag) / 2
            c_i -= 1
        if flag:
            ret += str(flag)
        return ret[::-1]  # Python没有提供直接反转字符串的函数，用切片凑合一下吧。

# easy: http://lintcode.com/zh-cn/problem/add-binary/
