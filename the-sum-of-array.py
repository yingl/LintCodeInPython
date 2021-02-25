class Solution:
    """
    @param arr: An array
    @return: An array
    """
    def getSum(self, arr):
        # Write your code here.
        ret = []
        arr_copy = arr.copy()
        arr.sort()
        di = {}
        for i in arr:
            di[i] = 0
        for i in range(1, len(arr)):
            di[arr[i]] = arr[i - 1] + di[arr[i - 1]]
        for i in arr_copy:
            ret.append(di[i])
        return ret

# easy: https://www.lintcode.com/problem/the-sum-of-array/
