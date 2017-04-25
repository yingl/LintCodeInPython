# coding: utf-8

class Solution:
    # @param {int[]} nums1 an integer array
    # @param {int[]} nums2 an integer array
    # @return {int[]} an integer array
    def intersection(self, nums1, nums2):
        # Write your code here
        ret = []
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        while (i < len(nums1)) and (j < len(nums2)):
            if nums1[i] == nums2[j]:
                ret.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i+= 1
            else:
                j += 1
        return ret

# easy: http://lintcode.com/zh-cn/problem/intersection-of-two-arrays-ii/
