class Solution:
    """
    @param candies: a list of integers
    @return: return a integer
    """
    def distributeCandies(self, candies):
        # write your code here
        return min(len(set(candies)), int(len(candies) / 2))

# easy: https://www.lintcode.com/problem/distribute-candies/
