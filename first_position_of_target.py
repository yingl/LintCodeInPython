# coding: utf-8

class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        # write your code here
        begin, end = 0, len(nums)
        while begin <= end:
            mid = (begin + end) / 2
            if nums[mid] < target:
                begin = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                # 这里其实可以用二分法继续优化！
                for i in xrange(mid - 1, -1, -1):
                    if nums[i] != target:
                        return i + 1
                return 0
        return -1

# easy: http://lintcode.com/zh-cn/problem/first-position-of-target/
