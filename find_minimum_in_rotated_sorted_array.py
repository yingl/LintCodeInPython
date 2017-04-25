# coding: utf-8

class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        # write your code here
        if len(num) == 1:
            return num[0]
        low = 1
        high = len(num) - 1
        while low < high:
            mid = (low + high) / 2
            if (num[mid] < num[mid - 1]) and (num[mid] < num[mid + 1]):
                return num[mid]
            elif num[mid] > num[0]:
                low += 1
            else:
                high -= 1
        return min(num[0], num[-1])

# medium: http://lintcode.com/zh-cn/problem/find-minimum-in-rotated-sorted-array/
