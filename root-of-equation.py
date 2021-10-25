class Solution:
    """
    @param a: parameter of the equation
    @param b: parameter of the equation
    @param c: parameter of the equation
    @return: a double array, contains at most two root
    """
    def rootOfEquation(self, a, b, c):
        # write your code here
        r = b * b - 4 * a * c
        if r < 0:
            return []
        elif r == 0:
            return [-b / (a * 2)]
        else:
            r = math.sqrt(r)
            if a > 0:
                return [(-b - r) / (a * 2), (-b + r) / (a * 2)]
            else:
                return [(-b + r) / (a * 2), (-b - r) / (a * 2)]
              
# easy: https://www.lintcode.com/problem/239/
