class Solution:
    """
    @param a: a integer represent the length of one edge
    @param b: a integer represent the length of one edge
    @param c: a integer represent the length of one edge
    @return: whether three edges can form a triangle
    """
    def isValidTriangle(self, a, b, c):
        # write your code here
        lines = sorted([a, b, c])
        return ((lines[0] + lines[1]) > lines[2]) \
               and ((lines[2] - lines[1]) < lines[0])

# easy: https://www.lintcode.com/problem/valid-triangle/
