class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # write your code here
        ret = []
        for i in range(len(nums), -1, -1):
            self.adjustDown(nums, len(nums), i)
        for i in range(1, k + 1):
            ret.append(nums[0])
            nums[0] = nums[-i]
            self.adjustDown(nums, len(nums) - i, 0)
        return ret
    
    def adjustDown(self, nums, size, i):
        while i < size:
            left = i * 2 + 1
            right = i * 2 + 2
            max_pos = i
            if (left < size) and (nums[left] > nums[max_pos]):
                max_pos = left
            if (right < size) and (nums[right] > nums[max_pos]):
                max_pos = right
            if max_pos != i:
                nums[i], nums[max_pos] = nums[max_pos], nums[i]
                i = max_pos
            else:
                break

# medium: https://www.lintcode.com/problem/top-k-largest-numbers/
