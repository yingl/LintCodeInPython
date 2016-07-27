# -*- coding: utf-8 -*-

class Solution:
    """
    @param {int} n an integer.
    @return {int} the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        numbers = [1] * n # 初始值
        index_2 = 0 # 对应乘235的最小值索引
        index_3 = 0
        index_5 = 0
        for i in xrange(1, n):
            m_2 = 2 * numbers[index_2]
            m_3 = 3 * numbers[index_3]
            m_5 = 5 * numbers[index_5]
            numbers[i] = min(min(m_2, m_3), m_5)
            index_2 += 1 if numbers[i] >= m_2 else 0
            index_3 += 1 if numbers[i] >= m_3 else 0
            index_5 += 1 if numbers[i] >= m_5 else 0
        return numbers[-1]