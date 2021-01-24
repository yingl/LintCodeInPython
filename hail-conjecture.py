class Solution:
    """
    @param num: an integer
    @return: return an integer
    """
    def getAnswer(self, num):
        # write your code here.
        ret = 0
        while num != 1:
            if (num % 2) == 0:
                num /= 2
            else:
                num = num * 3 + 1
            ret += 1
        return ret
        
# easy: https://www.lintcode.com/problem/hail-conjecture/
