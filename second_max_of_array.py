class Solution:
    """
    @param nums: An integer array
    @return: The second max number in the array.
    """
    @staticmethod
    def update(data, value):
        m = min(data)
        if data[0] == m:
            pos = 0
        else:
            pos = 1
        if value > data[pos]:
            data[pos] = value # 更新比较小的那个数

    def secondMax(self, nums):
        # write your code here
        data = nums[0:2]
        for i in range(2, len(nums)):
            Solution.update(data, nums[i])
        return min(data)

# easy: https://www.lintcode.com/problem/second-max-of-array
