# coding: utf-8

class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        # write your code here
        start, end = 0, len(A) - 1
        while start <= end:
            mid = (start + end) / 2
            if A[mid] == target:
                return mid
            '''
            注意，因为数组是旋转排序，所以先不要与target比较。
            1. 如股票A[mid] >= A[start]，那么A[mid]肯定在前半个上升序列。
            2. 反之A[mid]则在后半个上升序列。
            '''
            elif A[start] <= A[mid]:
                if (A[start] <= target) and (A[mid] > target):
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if (A[end] >= target) and (A[mid] < target):
                    start = mid + 1
                else:
                    end = mid - 1
        return -1

# medium: http://lintcode.com/zh-cn/problem/search-in-rotated-sorted-array/
