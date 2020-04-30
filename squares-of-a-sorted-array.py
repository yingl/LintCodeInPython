class Solution:
    """
    @param A: The array A.
    @return: The array of the squares.
    """
    def SquareArray(self, A):
        #
        ret = []
        for i in A:
            ret.append(i * i)
        ret.sort()
        return ret

# easy: https://www.lintcode.com/problem/squares-of-a-sorted-array/
