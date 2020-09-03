class Solution:
    """
    @param steps: steps you can move
    @param arrLen: the length of the array
    @return: Number of Ways to Stay in the Same Place After Some Steps
    """
    def numWays(self, steps, arrLen):
        # write your code here
        # DP: 第i步到位置j的方案可以根据之前状态推出
        # dp[i][j] = dp[i-1][j] +   ~ 不动
        #            dp[i-1][j+1] + ~ 向左
        #            dp[i-1][j-1]   ~ 向右
        dist = min(steps, arrLen) # 最远可以到位置cols
        dp = [[0 for i in range(dist)] for i in range(steps + 1)] # 第0步到第steps步
        dp[0][0] = 1
        for step in range(1, steps + 1):
            for d in range(dist):
                if d == 0:
                    dp[step][d] += dp[step - 1][d]
                    if (d + 1) < dist:
                        dp[step][d] += dp[step - 1][d + 1] # 可以向左一步回到0点
                elif d == (dist - 1):
                    dp[step][d] += dp[step - 1][d] + dp[step - 1][d - 1] # 可以向向一步到终点
                else:
                    dp[step][d] += dp[step - 1][d] + dp[step - 1][d + 1] + dp[step - 1][d - 1]
        return dp[steps][0] % (pow(10, 9) + 7)

# easy: https://www.lintcode.com/problem/number-of-ways-to-stay-in-the-same-place-after-some-steps-i/
