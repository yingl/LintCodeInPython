class Solution:
    """
    @param arr: an array of integers
    @return: return the biggest value X, which occurs in A exactly X times.
    """
    def findX(self, arr):
        # write your code here
        ret = 0
        di = {}
        for i in arr:
            if i not in di:
                di[i] = 0
            di[i] += 1
        for k, v in di.items():
            if k == v:
                if k > ret:
                    ret = k
        return ret
        
# easy: https://www.lintcode.com/problem/largest-number-x-which-occurs-x-times/
