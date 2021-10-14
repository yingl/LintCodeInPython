class Solution:
    """
    @param a: the array a
    @return: return the maximum value
    """
    def getAnswer(self, a):
        # Write your code here
        r = 0
        for i in range(len(a)):
            if (a[i] % 2) == 0:
                for j in range(i - 1, -1, -1):
                    if (a[j] % 2) == 1:
                        r = max(r, a[i] - a[j])
        return r
      
# easy: https://www.lintcode.com/problem/1617
