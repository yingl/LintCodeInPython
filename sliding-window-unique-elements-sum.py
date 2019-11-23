class Solution:
    """
    @param nums: the given array
    @param k: the window size
    @return: the sum of the count of unique elements in each window
    """
    def slidingWindowUniqueElementsSum(self, nums, k):
        # write your code here
        ret = 0
        uniques = 0
        di = {}
        window_size = k
        if k > len(nums):
            window_size = len(nums)
        # 初始化窗口
        for i in range(0, window_size):
            if nums[i] not in di:
                di[nums[i]] = 1
                uniques += 1
            else:
                if di[nums[i]] == 1:
                    uniques -= 1
                di[nums[i]] += 1
        ret += uniques
        for i in range(k, len(nums)):
            prev_num = nums[i - k]
            di[prev_num] -= 1
            if di[prev_num] == 1: # 上一个数字从不unique因为滑动再次unique
                uniques += 1
            elif di[prev_num] == 0: # 上一个数字因为unique滑动出去没有了
                uniques -= 1
            if (nums[i] not in di) or (di[nums[i]] == 0): # 新滑动进来的数字符合unique条件
                di[nums[i]] = 1
                uniques += 1
            else:
                if di[nums[i]] == 1: # 新滑动进来的数字从unique变成不符合条件
                    uniques -= 1
                di[nums[i]] += 1
            ret += uniques
        return ret

# https://www.lintcode.com/problem/sliding-window-unique-elements-sum
