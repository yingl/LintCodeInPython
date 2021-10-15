class Solution:
    """
    @param nums: the arrays
    @param k: the distance of the same number
    @return: the ans of this question
    """
    def sameNumber(self, nums, k):
        # Write your code here
        di = {}
        for i in range(len(nums)):
            if nums[i] not in di:
                di[nums[i]] = i
            else:
                if (i - di[nums[i]]) < k:
                    return 'YES'
        return 'NO'
      
# easy: https://www.lintcode.com/problem/1368/
