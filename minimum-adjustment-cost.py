# coding: utf-8

class Solution:
    # @param A: An integer array.
    # @param target: An integer.
    def MinAdjustmentCost(self, A, target):
        # write your code here
        '''
        动态规划，重要的限制条件是最大的数小于等于100！
        我们用d[i][j]表示第i个元素调整到j的最小代价。所以最后结果就是d[i][0]到d[100]取最小值。
        '''
        if len(A) < 2:
            return 0
        costs = [[2147483647 for i in xrange(101)] for j in xrange(len(A))]
        for i in xrange(101): # 初始化第一行
            costs[0][i] = abs(A[0] - i)
        for i in xrange(1, len(A)):
            for j in xrange(0, 101):
                diff = abs(A[i] - j)  # A[i]调整到j的成本
                begin = max(0, j - target)  # 相对于j，A[i - 1]的取值下限
                end = min(100, j + target) # 相对于j，A[i - 1]的取值上限
                for k in xrange(begin, end + 1):
                    '''
                    重点！
                    costs[i - 1][j]代表第u - 1个元素调整到k的最小代价，
                    k + diff - A[i]确保范围在target以内。
                    '''
                    costs[i][j] = min(costs[i][j], costs[i - 1][k] + diff)
        ret = 2147483647
        for i in xrange(0, 101):
            ret = min(ret, costs[len(A) - 1][i])
        return ret

# medium: http://lintcode.com/zh-cn/problem/minimum-adjustment-cost/
