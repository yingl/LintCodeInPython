class Solution:
    """
    @param arr: An array
    @return: A boolean
    """
    def isUnique(self, arr):
        # write your code here
        n = len(arr)
        return sum(arr) == int((n - 1) * n / 2)
      
# medium: https://www.lintcode.com/problem/571/
