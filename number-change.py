class Solution:
    """
    @param k: integer k
    @return: minimum number of operations that change 0 to k
    """
    def numberChange(self, k):
        # write your code here
        if k == 0:
            return 0
        else:
            if (k % 2) == 0:
                return 1 + self.numberChange(int(k/2))
            else:
                return 1 + self.numberChange(k - 1)
              
# medium: https://www.lintcode.com/problem/1825/
