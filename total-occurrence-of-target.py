class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def totalOccurrence(self, A, target):
        # write your code here
        i = self.bSearch(A, target)
        if i == -1:
            return 0
        start = self.fMin(A, 0, i, target)
        end = self.fMax(A, i, len(A) - 1, target)
        if start == -1:
            start = 0
        if end == -1:
            end = len(A) - 1
        return end - start + 1

    def bSearch(self, A, target):
        i, j = 0, len(A) - 1
        while i <= j:
            mid = int((i + j) / 2)
            if A[mid] > target:
                j = mid - 1
            elif A[mid] < target:
                i = mid + 1
            else:
                return mid
        return -1

    def fMin(self, A, start, end, target):
        i, j = start , end
        while i <= j:
            mid = int((i + j) / 2)
            if A[mid] < target:
                if (mid < end) and (A[mid + 1] == target):
                    return mid + 1
                else:
                    i = mid + 1
            else:
                j = mid - 1
        return -1

    def fMax(self, A, start, end, target):
        i, j = start , end
        while i <= j:
            mid = int((i + j) / 2)
            if A[mid] > target:
                if (start < mid) and (A[mid - 1] <= target):
                    return mid - 1
                else:
                    j = mid - 1
            else:
                i = mid + 1
        return -1
        
# easy: https://www.lintcode.com/problem/462/
