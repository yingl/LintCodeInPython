class Solution:
    """
    @param arr: a integer array
    @return: return the unique array
    """
    def getUniqueArray(self, arr):
        # write your code here
        s = set([])
        dups = 0
        for i in range(len(arr)):
            v = arr[i]
            if v not in s:
                s.add(v)
                arr[i - dups] = v
            else:
                dups += 1
        return arr[:-dups]
        
# easy: https://www.lintcode.com/problem/unique-array/
