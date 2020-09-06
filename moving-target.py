class Solution:
    """
    @param nums: a list of integer
    @param target: an integer
    @return: nothing
    """
    def MoveTarget(self, nums, target):
        # write your code here
        steps = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == target:
                steps += 1
            else:
                nums[i + steps] = nums[i]
        for i in range(steps):
            nums[i] = target
        return nums
        
# easy: https://www.lintcode.com/problem/moving-target/
