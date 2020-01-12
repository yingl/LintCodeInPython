class Solution:
    """
    @param num: the num
    @return: the array subject to the description
    """
    def calculateNumber(self, num):
        # Write your code here.
        ret = []
        count, pos = 0, 0
        while num != 0:
            if (num % 2) != 0:
                ret.append(pos)
                count += 1
            num = int(num / 2)
            pos += 1
        ret.append(count)
        ret.reverse()
        for i in range(1, len(ret)):
            ret[i] = pos - ret[i]
        return ret
        
# easy: https://www.lintcode.com/problem/calculate-number/
