class Solution:
    """
    @param N: a positive number
    @return: how many numbers X from 1 to N are good
    """
    def rotatedDigits(self, N):
        # write your code here
        ret = 0
        for n in range(1, N+1):
            ret += self.check(n)
        return ret

    def check(self, n):
        ret = 0
        while n > 0:
            i = n % 10
            n = int(n / 10)
            if i in [3, 4, 7]:
                return 0
            elif i in [2, 5, 6, 9]:
                ret = 1
        return ret

# easy: https://www.lintcode.com/problem/rotated-digits/
