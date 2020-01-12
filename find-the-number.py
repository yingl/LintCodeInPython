class Solution:
    """
    @param nums: a integer array
    @param k: a integer
    @return: return true or false denoting if the element is present in the array or not
    """
    def findnNumber(self, nums, k):
        # write your code here
        for i in nums:
            if k == i:
                return True
        return False
        
# easy: https://www.lintcode.com/problem/find-the-number/
