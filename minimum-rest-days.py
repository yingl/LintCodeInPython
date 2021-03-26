class Solution:
    """
    @param company: Company business
    @param gym: Gym business
    @return: Find the shortest rest day
    """
    def minimumRestDays(self, company, gym):
        # write your code here
        days = len(company)
        ret = days
        '''
        第0行：工作
        第1行：健身
        第2行：休息
        dp[0][i]表示第i天工作情况下最小休息几天，同理可推dp[1][i]和dp[2][i]。
        '''
        dp = [[0, 0], [0, 0], [0, 0]] # 滚动数组比较省空间
        dp[0][0] = 0 if company[0] == 1 else 1 # 第0天如果工作最小只休息0天...
        dp[1][0] = 0 if gym[0] == 1 else 1
        dp[2][0] = 1
        for i in range(1, days):
            t = i & 1 # today
            y = (i - 1) & 1 # yesterday
            dp[0][t] = dp[1][t] = dp[2][t] = days # 初始化，利用i & 1实现两天交错。
            if company[i] == 1: # 今天可以工作
                dp[0][t] = dp[2][y] # 如果昨天可以休息的话，休息天数不会比昨天可以休息更多！！！
                if gym[i - 1] == 1:
                    dp[0][t] = min(dp[0][t], dp[1][y]) # 如果昨天健身的话，今天可以上班，所以休息天数选择较小的那个。
            if gym[i] == 1:
                dp[1][t] = dp[2][y]
                if company[i - 1] == 1:
                    dp[1][t] = min(dp[1][t], dp[0][y])
            for j in range(3):
                dp[2][t] = min(dp[2][t], dp[j][y] + 1) # 因为每天都可能休息，所以dp[j][y]要加1!
        for i in range(3):
            ret = min(ret, dp[i][(days - 1) & 1])
        return ret
      
# medium: https://www.lintcode.com/problem/minimum-rest-days
