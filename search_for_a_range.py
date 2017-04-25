# coding: utf-8

class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        i = self.bSearch(A, 0, len(A), target)
        if i == -1:
            return [-1, -1]
        start, end = i, i
        while i != -1:  # 前半区不停二分，直到找不到target为止
            start = i
            i = self.bSearch(A, 0, start, target)
        if end < len(A) - 1:
            i = end
            while (i != -1) and (i <= (len(A) - 1)):
                end = i
                i = self.bSearch(A, end + 1, len(A), target)
                if i == -1:
                    break
        return [start, end]
        
    def bSearch(self, array, start, end, target):
        while start < end:
            mid = (start + end) / 2
            if array[mid] == target:
                return mid
            elif array[mid] < target:
                start = mid + 1
            else:
                end = mid   # end是开区间，所以不用减1。
        return -1

# medium: http://lintcode.com/zh-cn/problem/search-for-a-range/
