class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def firstUniqueNumber(self, nums, number):
        # Write your code here
        # 难度在于第一个
        di = {}
        pos = 0
        for i in range(0, len(nums)):
            if nums[i] == number:
                min_pos = len(nums)
                items = sorted(di.items(), key = lambda item: item[1]) # 根据位置排序
                if items and (items[0][1] < len(nums)):
                    return items[0][0]
                else:
                    return number
            else:
                if nums[i] not in di: # 来，先看这里的注释。
                    di[nums[i]] = pos # 记录第一次出现的位置
                    pos += 1
                else:
                    di[nums[i]] = len(nums) # 重复了就把位置挪到最后
        return -1

# medium: https://www.lintcode.com/problem/first-unique-number-in-data-stream
