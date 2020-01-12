class Solution:
    """
    @param nums: List[List[int]]
    @param r: an integer
    @param c: an integer
    @return: return List[List[int]]
    """
    def matrixReshape(self, nums, r, c):
        # write your code here
        old_row, old_col = len(nums), len(nums[0])
        if (r * c) != (old_row * old_col):
            return nums
        ret = [[0] * c for i in range(r)]
        for i in range(old_row):
            for j in range(old_col):
                idx = i * old_col + j
                ret[int(idx / c)][idx % c] = nums[i][j]
        return ret

# easy: https://www.lintcode.com/problem/reshape-the-matrix/
