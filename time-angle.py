class Solution:
    """
    @param h: hours
    @param m: minutes
    @return: angle between hour hand and minute hand at X:Y in a clock
    """
    def timeAngle(self, h, m):
        # write your code here
        h = h * 5 + m / 12
        ret = abs(h - m) * 6
        if ret > 180:
            return 360 - ret
        else:
            return ret
            
# easy: https://www.lintcode.com/problem/time-angle/
