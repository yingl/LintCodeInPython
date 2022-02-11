class Solution:
    """
    @param arr: the line 
    @param k: Alex place
    @return: the time when Alex requires to buy all passes
    """
    def buyPasses(self, arr, k):
        # Write your code here.
        r = 0
        for i in range(len(arr)):
            if i <= k:
                r += min(arr[i], arr[k])
            else:
                r += min(arr[k] - 1, arr[i])
        return r
        
'''
arr = [1, 2, 5] means they want 1, 2, 5 tickets.
k = 1 means Alex is user 1 who needs 2 tickets.
'''

# medium: https://www.lintcode.com/problem/1851/
