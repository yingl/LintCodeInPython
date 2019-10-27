class Solution:
    """
    @param num: an integer
    @return: returns true when it is a perfect number and false when it is not
    """
    def checkPerfectNumber(self, num):
        # write your code here
        if num == 1:
            return False
        ret = 1
        i = 2
        while i * i <= num:
            if num % i == 0:
                ret += (i + int(num / i))
            i += 1
        return ret == num
                
# easy: https://www.lintcode.com/problem/perfect-number/
