class Solution:
    """
    @param lower: Integer : lower bound
    @param upper: Integer : upper bound
    @return: a list of every possible Digit Divide Numbers
    """
    def digitDivideNums(self, lower, upper):
        # write your code here
        ret = []
        i = lower
        while i <= upper:
            tmp = i
            while i > 0:
                v = i % 10
                if v == 0:
                    break
                else:
                    if (tmp % v) == 0:
                        i = int(i / 10)
                    else:
                        break
            if i == 0:
                ret.append(tmp)
            i = tmp + 1
        return ret
        
# medium: https://www.lintcode.com/problem/self-dividing-numbers/
