class Solution:
    """
    @param nums: a binary array
    @return:  the maximum number of consecutive 1s
    """
    def findMaxConsecutiveOnes(self, nums):
        # Write your code here
        ret = 0
        count = 0
        for i in nums:
            if i == 0:
                if count > 0:
                    if count > ret:
                        ret = count
                    count = 0
            else:
                count += 1
        return max(ret, count)

# easy: https://www.lintcode.com/problem/max-consecutive-ones/
