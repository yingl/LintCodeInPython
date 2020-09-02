class Solution:
    """
    @param A: an array
    @return: any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
    """
    def peakIndexInMountainArray(self, A):
        # Write your code here
        # 二分法，找到一个满足比左右元素都大的元素即可。
        left, right = 0, len(A) - 1
        while left < right:
            mid = left + int((right - left) / 2)
            if A[mid] < A[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return right


# easy: https://www.lintcode.com/problem/peak-index-in-a-mountain-array/
