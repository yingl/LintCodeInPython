# coding: utf-8

class Solution:
    # @param {int[]} nums1 an integer array
    # @param {int[]} nums2 an integer array
    # @return {int[]} an integer array
    def intersection(self, nums1, nums2):
        # Write your code here
        nums1.sort()
        nums2.sort()
        self.ret = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if len(self.ret) == 0:
                    self.ret.append(nums1[i])
                elif nums1[i] != self.ret[-1]:
                        self.ret.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return self.ret

# easy: http://lintcode.com/zh-cn/problem/intersection-of-two-arrays/
