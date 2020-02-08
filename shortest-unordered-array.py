class Solution:
    """
    @param arr: an array of integers
    @return: the length of the shortest possible subsequence of integers that are unordered
    """
    def shortestUnorderedArray(self, arr):
        # write your code here
        order = arr[1] > arr[0] # 升序：True
        if order:
            for i in range(1, len(arr) - 1):
                if arr[i + 1] < arr[i]:
                    return 3
        else:
            for i in range(1, len(arr) - 1):
                if arr[i + 1] > arr[i]:
                    return 3
        return 0
            
# easy: https://www.lintcode.com/problem/shortest-unordered-array/
