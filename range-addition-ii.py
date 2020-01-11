class Solution:
    """
    @param m: an integer
    @param n: an integer
    @param ops: List[List[int]]
    @return: return an integer
    """
    def maxCount(self, m, n, ops):
        # write your code here
        if not ops:
            return m * n
        ops = zip(*ops)
        return min(ops[0]) * min(ops[1])

# easy: https://www.lintcode.com/problem/range-addition-ii/
