class Solution:
    """
    @param nums: a non-empty array only positive integers
    @return: true if can partition or false
    """
    def canPartition(self, nums):
        # write your code here
        '''
        1. 和为奇数一定不行
        2. 和为偶数，使用DP,状态矩阵为dp[i][j],代表前i个元素能否构造和j。状态转移方程如下（索引从0开始算）：
           - 状态1：dp[i - 1][j - nums[i - 1]] -> dp[i][j]
           - 状态2：dp[i - 1][j] -> dp[i][j]
        '''
        nums_sum = sum(nums)
        if (nums_sum % 2) != 0:
            return False
        nums_sum = int(nums_sum / 2)
        nums_len = len(nums)
        dp = [[False] * (nums_sum + 1) for i in range(nums_len + 1)]
        for i in range(nums_len + 1):
            dp[i][0] = True # 0个元素就构造和为0
        for i in range(1, nums_len + 1):
            for j in range(1, nums_sum + 1):
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[nums_len][nums_sum]

# medium: https://www.lintcode.com/problem/partition-equal-subset-sum/
