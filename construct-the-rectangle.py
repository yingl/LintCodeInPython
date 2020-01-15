class Solution:
    """
    @param area: web pageâs area
    @return: the length L and the width W of the web page you designed in sequence
    """
    def constructRectangle(self, area):
        # Write your code here
        ret = []
        diff = area
        for w in range(1, area + 1):
            if area % w == 0:
                l = int(area / w)
                if w > l:
                    break
                if (l - w) < diff:
                    diff = l - w
                    ret = [l, w]
        return ret

# easy: https://www.lintcode.com/problem/construct-the-rectangle/
