class Solution:
    """
    @param heights: Students height
    @return: How many people are not where they should be
    """
    def orderCheck(self, heights):
        # write your code here
        ret = 0
        sorte_heights = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != sorte_heights[i]:
                ret += 1
        return ret
        
# easy: https://www.lintcode.com/problem/order-check/
