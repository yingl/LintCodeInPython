class Solution:
    """
    @param A: an integer array sorted in ascending order
    @param target: An integer
    @return: an integer
    """
    def closestNumber(self, A, target):
        # write your code here
        x, y, z = -1, -1, -1
        i, j = 0, len(A) - 1
        while i <= j:
            mid = int((i + j) / 2)
            if A[mid] < target:
                if (mid < (len(A) - 1)) and (A[mid + 1] >= target):
                    y = mid
                i = mid + 1
            elif A[mid] > target:
                if (0 < mid) and (A[mid - 1] <= target):
                    z = mid
                j = mid - 1
            else:
                x = mid
                break
        if x != -1:
            return x
        if (y == -1) and (A[-1] < target):
                return len(A) - 1
        if (z == -1) and (A[0] > target):
                return 0
        return y if (target - A[y]) <= (A[z] - target) else z
      
# easy: https://www.lintcode.com/problem/459
