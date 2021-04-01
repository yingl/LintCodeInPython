class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        start, end = 0, len(nums) - 1
        while (start < end) and (nums[start] >= nums[end]): # 结果肯定在start和end中间某个位置
          mid = (start + end) // 2
          if nums[start] < nums[mid]: # mid在前半区间
            start = mid + 1
          elif nums[start] > nums[mid]: # mid在后半区间
            end = mid # 不用减一，有可能就是这个位置。
          else:
            start += 1 # 重复元素的特殊情况
        return nums[start]

# medium: https://www.lintcode.com/problem/find-minimum-in-rotated-sorted-array-ii/
