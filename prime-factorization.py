class Solution:
    """
    @param num: An integer
    @return: an integer array
    """
    def primeFactorization(self, num):
        # write your code here
        ret = []
        i = 2
        while i * i <= num:
            if (num % i) == 0:
                ret.append(i)
                num = int(num / i)
                i = 2
            else:
                i += 1
        if num > 0:
            ret.append(num)
        return ret
      
# easy: https://www.lintcode.com/problem/235
