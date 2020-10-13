class Solution:
    """
    @param circles: The value of 6 points on n rings
    @return: Whether there are two same circles
    """
    def samecircle(self, circles):
        # write your code here
        s = set()
        for circle in circles:
            circle.sort()
            _circle = '-'.join([str(c) for c in circle])
            if _circle in s:
                return True
            else:
                s.add(_circle)
        return False
        
# easy: https://www.lintcode.com/problem/circle/
