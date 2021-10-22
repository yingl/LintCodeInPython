class Solution:
    """
    @param nums: the integers to be paired.
    @return: return the minimum difference of the maximum value and the minimum value after pairing.
    """
    def digitalPairing(self, nums):
        # write your code here.
        nums.sort()
        l = len(nums)
        for i in range(int(l / 2)):
            nums[i] += nums[- 1]
            nums.pop()
        nums.sort()
        return nums[-1] - nums[0]
      
# easy: https://www.lintcode.com/problem/302/
