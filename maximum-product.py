class Solution:
    """
    @param nums: Unordered array
    @return: return the largest product
    """
    def MaximumProduct(self, nums):
        # write your code here
        nums.sort()
        if len(nums) < 3:
            return 0
        return max( nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
        
# medium: https://www.lintcode.com/problem/maximum-product/
