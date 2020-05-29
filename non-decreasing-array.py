class Solution:
    """
    @param nums: an array
    @return: if it could become non-decreasing by modifying at most 1 element
    """
    def checkPossibility(self, nums):
        # Write your code here
        k = -1
        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i]:
                k = i + 1 # 可疑，需要处理！
                break
        if k > 0:
            if k == 1:
                prev = nums[k] # 要考虑出现的第一个元素就比后面大的情况
            else:
                prev = nums[k - 2] # 比较基准
            print(k, prev)
            for i in range(k, len(nums)):
                if nums[i] < prev:
                    return False
                prev = nums[i]
        return True

# https://www.lintcode.com/problem/non-decreasing-array/
