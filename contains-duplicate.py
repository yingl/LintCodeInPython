class Solution:
    """
    @param nums: the given array
    @return: if any value appears at least twice in the array
    """
    def containsDuplicate(self, nums):
        # Write your code here
        nums = sorted(nums)
        if len(nums) > 1:
            for i in range(1, len(nums)):
                if nums[i] == nums[i - 1]:
                    return True
        return False

# easy: https://www.lintcode.com/problem/contains-duplicate/
