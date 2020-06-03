class Solution:
    """
    @param nums: an integer array
    @return: the maximum product
    """
    def maximumProduct(self, nums):
        # Write your code here
        '''
        其实不用考虑正负号的情，先排序,然后比以下两种情况：
        1. 最大的3个数相乘
        2. 最小的两数承最大的数
        '''
        nums.sort()
        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])
        
# easy: https://www.lintcode.com/problem/maximum-product-of-three-numbers/description
