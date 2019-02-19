class Solution:
    """
    @param num: a positive integer
    @return: if num is a perfect square else False
    """
    def isPerfectSquare(self, num):
        # write your code here
        i, j = 0, num
        while i <= j:
            k = int((i + j) / 2) # 二分收敛
            k2 = k * k
            if k2 == num:
                return True
            elif k2 > num:
                j = k - 1
            else:
                i = k + 1
        return False

# easy: https://www.lintcode.com/problem/valid-perfect-square
