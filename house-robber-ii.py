class Solution:
    """
    @param nums: An array of non-negative integers.
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber2(self, nums):
        # write your code here
        # 第一间与最后一间不能同时抢
        if (not nums) or (len(nums) == 2):
            return 0
        if len(nums) == 1:
            return nums[0]
        dp_1 = [0] * (len(nums) - 1) # 0到倒数第2间
        dp_2 = [0] * (len(nums) - 1) # 1到最后一间
        for i in range(0, len(nums) - 1):
            if i == 0:
                dp_1[i] = nums[0]
            if i == 1:
                dp_1[i] = max(nums[0], nums[1])
            if i > 1:
                dp_1[i] = max(dp_1[i - 2] + nums[i], dp_1[i - 1])
        for i in range(1, len(nums)):
            if i == 1:
                dp_2[i - 1] = nums[1]
            if i == 2:
                dp_2[i - 1] = max(nums[1], nums[2])
            if i > 2:
                dp_2[i - 1] = max(dp_2[i - 3] + nums[i], dp_2[i - 2])
        return max(dp_1[-1], dp_2[-1])

# medium: http://lintcode.com/zh-cn/problem/house-robber-ii/
