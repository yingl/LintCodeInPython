class Solution:
    """
    @param cost: an array
    @return: minimum cost to reach the top of the floor
    """
    def minCostClimbingStairs(self, cost):
        # Write your code here
        '''
        可以从0阶开始，也可以从一阶开始，所以状态数组前2个值为0。
        对于第n级台阶，可以从n - 1级，也可以从n - 2级台阶抵达，所以方程如下：
        dp[n] = min(dp[n - 1] + cost[n - 1], dp[n - 2] + cost[n - 2)
        注意：如果cost长度为3，那么我们的目标是第3级台阶（索引从0开始）。
        '''
        ret = [0] * (len(cost) + 1)
        for i in range(2, len(ret)):
            ret[i] = min(ret[i - 1] + cost[i - 1], ret[i - 2] + cost[i - 2])
        return ret[-1]

# easy: https://www.lintcode.com/problem/min-cost-climbing-stairs/
