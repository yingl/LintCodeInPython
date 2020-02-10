class Solution:
    """
    @param nums: a list of integers
    @return: return a list of integers
    """
    def findDisappearedNumbers(self, nums):
        # write your code here
        ret = []
        i = 0
        while i < len(nums):
            if nums[i] != nums[nums[i] - 1]: # 当前元素的值与索引不匹配
                tmp = nums[nums[i] - 1] # 保留原来位置的值
                nums[nums[i] - 1] = nums[i]
                nums[i] = tmp
                i -= 1 # 换过来的元素再处理
            i += 1
        for i in range(len(nums)):
            if nums[i] != (i + 1):
                ret.append(i + 1)
        return ret

# easy: https://www.lintcode.com/problem/find-all-numbers-disappeared-in-an-array/
