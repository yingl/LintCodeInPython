class Solution:
    """
    @param r: a Integer represent radius
    @return: the circle's circumference nums[0] and area nums[1]
    """
    def calculate(self, r):
        # write your code here
        pi = 3.14
        c = int(pi * 2.0 * r * 100.0)
        s = int(pi * r * r * 100.0)
        return [c / 100.0, s / 100.0]

easy: https://www.lintcode.com/problem/calculate-circumference-and-area
