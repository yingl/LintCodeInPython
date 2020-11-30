class Solution:
    """
    @param arr: an inter array 
    @return: return the min sum
    """
    def splitArray(self, arr):
        # write your code here
        nums = []
        for i in range(1, len(arr) - 1):
            if len(nums) < 3:
                nums.append([arr[i], i])
                nums = sorted(nums, key=lambda x: x[0])
            else:
                for j in range(2, -1, -1):
                    if nums[j][0] > arr[i]:
                        nums[j] = [arr[i], i]
                        nums = sorted(nums, key=lambda x: x[0])
                        break
        nums = sorted(nums, key=lambda x: x[1])
        v1, v2, v3 = 100000000000, 100000000000, 100000000000
        if (nums[1][1] - nums[0][1]) > 1:
            v1 = nums[0][0] + nums[1][0]
        v2 = nums[0][0] + nums[2][0]
        if (nums[2][1] - nums[1][1]) > 1:
            v3 = nums[1][0] + nums[2][0]
        return min(v1, v2, v3)
        
# easy: https://www.lintcode.com/problem/split-array/
