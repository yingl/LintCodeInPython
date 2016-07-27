# -*- coding: utf-8 -*-

class Solution:
    def __init__(self):
        self.cache = {}

    # @paramn n: An integer
    # @return: An integer
    def numTrees(self, n):
        if n <= 1:
            return 1
        else:
            if n in self.cache:
                return self.cache[n]
            else:
                sum = 0
                for i in xrange(1, n + 1):
                    left_num, right_num = 1, 1
                    if i > 0:
                        left_num = self.numTrees(i - 1) # 计算左子树数量
                    if i < n:
                        right_num = self.numTrees(n - i)  # 计算右子树数量
                    sum += left_num * right_num
                self.cache[n] = sum
        return self.cache[n]