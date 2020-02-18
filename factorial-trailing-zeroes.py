class Solution:
    """
    @param n: a integer
    @return: return a integer
    """
    def trailingZeroes(self, n):
        # write your code here
        ret = 0
        while n > 0:
            # 技巧，2 * 5 = 10，而且2总是比5多。
            n = int(n / 5)
            ret += n
        return ret

# easy: https://www.lintcode.com/problem/factorial-trailing-zeroes/
