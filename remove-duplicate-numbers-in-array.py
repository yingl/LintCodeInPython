class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        '''
        nums.sort()
        steps = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                steps += 1
            else:
                nums[i - steps] = nums[i]
        return len(nums) - steps
        '''
        s = set(nums)
        i = 0
        for v in s:
            nums[i] = v
            i += 1
        return len(s)
      
# easy: https://www.lintcode.com/problem/521
