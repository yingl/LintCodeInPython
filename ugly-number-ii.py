# coding: utf-8

class Solution:
    """
    @param {int} n an integer.
    @return {int} the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        '''
        实现分析：
        i = 1
            m_2 = 2
            m_3 = 3
            m_5 = 5
            numbers[1] = 2
            i_2 += 1 => 1
            i_3 = 0
            i_5 = 0
        i = 2
            m_2 = numbers[1] * 2 = 2 * 2 = 4
            m_3 = 3
            m_5 = 5
            numbers[2] = 3
            i_2 ＝ 1
            i_3 += 1 => 1
            i_5 = 0
        i = 3
            m_2 = numbers[1] * 2 ＝ 4
            m_3 = numbers[1] * 3 = 6
            m_5 = 5
            numbers[3] = 4
            i_2 += 1 => 2
            i_3 = 1
            i_5 = 0
        i = 4
            m_2 = numbers[2] * 2 = 6
            m_3 = numbers[1] * 3 = 6
            m_5 = 5
            numbers[4] = 5
            i_2 = 2
            i_3 = 1
            i_5 = 1
        i = 5
            m_2 = numbers[2] * 2 = 6
            m_3 = numbers[1] * 3 = 6
            m_5 = numbers[1] * 5 = 10
            numbers[5] = 6
        ......

        '''
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

# medium: http://lintcode.com/zh-cn/problem/ugly-number-ii/
