class Solution:
    """
    @param nums: List[int]
    @return: return List[str]
    """
    def findRelativeRanks(self, nums):
        # write your code here
        ret = []
        sorted_nums = sorted(nums)[::-1]
        di = {}
        for i in range(len(sorted_nums)):
            di[sorted_nums[i]] = i + 1
            if i < 3:
                di[sorted_nums[i]] = ['Gold Medal', 'Silver Medal', 'Bronze Medal'][i]
        for i in nums:
            ret.append(str(di[i]))
        return ret
        
# easy: https://www.lintcode.com/problem/relative-ranks/
