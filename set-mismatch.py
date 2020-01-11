class Solution:
    """
    @param nums: an array
    @return: the number occurs twice and the number that is missing
    """
    def findErrorNums(self, nums):
        # Write your code here
        ret = []
        di = {}
        for i in nums:
            if i not in di:
                di[i] = 1
            else:
                di[i] += 1
                ret.append(i)
        for i in range(1, len(nums) + 1):
            if i not in di:
                ret.append(i)
                break
        return ret

# easy: https://www.lintcode.com/problem/set-mismatch/
