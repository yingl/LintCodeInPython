class Solution:
    """
    @param obstacles: the tracks which obstacles are settled on.
    @return: return the minimum times to switch the track.
    """
    def trackSwitching(self, obstacles):
        # write your code here.
        n = len(obstacles)
        ret = n
        dp = [[0, 0], [0, 0], [0, 0]]
        dp[obstacles[0] - 1][0] = 1000000
        if obstacles[0] == 1:
            dp[1][0], dp[2][0] = 0, 1
        elif obstacles[0] == 2:
            dp[0][0], dp[2][0] = 1, 1
        elif obstacles[0] == 3:
            dp[0][0], dp[1][0] = 1, 0
        for i in range(1, n):
            pmin = min(dp[0][0], min(dp[1][0], dp[2][0]))
            r = obstacles[i] - 1
            for j in range(3):
                if j == r:
                    dp[j][1] = 1000000
                else:
                    if dp[j][0] != 1000000:
                        dp[j][1] = min(dp[j][0], pmin + 1)
                    else:
                        dp[j][1] = pmin + 1
            dp[0][0] = dp[0][1]
            dp[1][0] = dp[1][1]
            dp[2][0] = dp[2][1]
        return min(dp[0][0], min(dp[1][0], dp[2][0]))        
      
# medium: https://www.lintcode.com/problem/348
