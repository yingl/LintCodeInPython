# coding: utf-8

class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        '''
        如果没有0，1可以在第0个位置出现。
        如果只有1个2，2出现在最后一个位置
        '''
        one_pos, two_pos = 0, len(nums) - 1
        i = 0
        while i <= min(two_pos, len(nums) - 1):
            if nums[i] == 0:
                if i == one_pos:  # 位置相等先记下
                    i += 1
                else:
                    nums[i], nums[one_pos] = nums[one_pos], nums[i] # 如果有1就把1换到指定位置了
                one_pos += 1  # 1出现的位置向后移动一位
            elif nums[i] == 2:
                nums[i], nums[two_pos] = nums[two_pos], nums[i]
                two_pos -= 1  # 2出现的位置向前移动一位
            else:
                i += 1

# medium: http://lintcode.com/zh-cn/problem/sort-colors/
