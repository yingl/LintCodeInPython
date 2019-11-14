# coding: utf-8

class Solution:
    # @param {int[][]} costs n x 3 cost matrix
    # @return {int} an integer, the minimum cost to paint all houses
    def minCost(self, costs):
        # Write your code here
        # 计算出每一层选某个颜色的最小值
        if not costs:
            return 0
        curr_costs = costs[0]
        for cost in costs[1:]:
            tmp = []
            for i in xrange(3):
                '''
                这里充分利用了负数索引的性质
                i = 0: -1 = 2; -2 = 1
                i = 1: 0 = 0; -1 = 2
                i = 2: 1 = 1; 0 = 0
                '''
                tmp.append(cost[i] + min(curr_costs[i - 1], curr_costs[i - 2]))
            curr_costs = tmp
        return min(curr_costs)

# medium: http://lintcode.com/zh-cn/problem/paint-house/
