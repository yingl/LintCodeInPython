class Solution:
    """
    @param A: an integer ratated sorted array and duplicates are allowed
    @param target: An integer
    @return: a boolean 
    """
    def search(self, A, target):
        # write your code here
        start, end = 0, len(A) - 1
        while start <= end:
            mid = int((start + end) / 2)
            if A[mid] == target:
                return True
            m1, m2 = mid, mid
            while (m1 > start) and (A[m1] <= A[start]):
                m1 -= 1
                if A[m1] == target:
                    return True
            while (m2 < end) and (A[m2] >= A[end]):
                m2 += 1
                if A[m2] == target:
                    return True
            if (A[m1] >= target) and (A[start] <= target):
                end = m1 - 1
            elif (A[m2] <= target) and (A[end] >= target):
                start = m2 + 1
            else:
                break
        return False
        
# medium: https://www.lintcode.com/problem/search-in-rotated-sorted-array-ii/
