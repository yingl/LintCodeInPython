class Solution:
    """
    @param n: count lucky numbers from 1 ~ n
    @return: the numbers of lucky number
    """
    def luckyNumber(self, n):
        # Write your code here
        ret = 0
        for i in range(8, n + 1):
            e = False
            while i > 0:
                if (i % 10) == 8:
                    e = True
                    break
                else:
                    i = int(i / 10)
            if e:
                ret += 1
        return ret

# easy: https://www.lintcode.com/problem/lucky-number-eight/
