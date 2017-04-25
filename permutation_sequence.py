# coding: utf-8

class Solution:
    """
    @param n: n
    @param k: the k-th permutation
    @return: a string, the k-th permutation
    """
    def getPermutation(self, n, k):
        ret = ''
        digits = [i for i in xrange(1, n + 1)]  # 字母表
        factorials = [1]    # 阶乘表
        for i in xrange(1, n):
            factorials.append(factorials[i - 1] * i)
        for i in xrange(n - 1, -1, -1):
            pos = (k - 1) / factorials[i]   # 计算第一个元素的位置
            ret += str(digits[pos])
            del(digits[pos])    # 删除已使用的元素
            k -= (pos * factorials[i])
        return ret

# medium: http://lintcode.com/zh-cn/problem/permutation-sequence/
