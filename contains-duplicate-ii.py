class Solution:
    """
    @param nums: the given array
    @param k: the given number
    @return:  whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k
    """
    def containsNearbyDuplicate(self, nums, k):
        # Write your code here
        di = {}
        for i in range(len(nums)):
            if nums[i] in di:
                di[nums[i]].append(i)
            else:
                di[nums[i]] = [i]
        for _, v in di.items():
            if len(v) >= 2:
                for i in range(1, len(v)):
                    if (v[i] - v[i - 1]) <= k:
                        return True
        return False

# easy: https://www.lintcode.com/problem/contains-duplicate-ii/
