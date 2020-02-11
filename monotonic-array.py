class Solution:
    """
    @param A: a array
    @return: is it monotonous
    """
    def isMonotonic(self, A):
        # Write your code here.
        if len(A) < 2:
            return True
        _dir = True # 记录方向
        i = 1
        while i < len(A):
            if A[i - 1] < A[i]:
                _dir = -1
                break
            elif A[i - 1] > A[i]:
                _dir = 1
                break
            i += 1
        for j in range(i, len(A) - 1):
            if _dir == -1:
                if A[j] > A[j + 1]:
                    return False
            else:
                if A[j] < A[j + 1]:
                    return False
        return True

# easy: https://www.lintcode.com/problem/monotonic-array/
