class Solution:
    """
    @param points: List[List[int]]
    @return: return a double
    """
    def largestTriangleArea(self, points):
        # write your code here
        ret = 0
        for i in range(len(points) - 2):
            for j in range(i + 1, len(points) - 1):
                for k in range(j + 1, len(points)):
                    area = 0.5 * abs(points[i][0] * points[j][1] \
                                     + points[j][0] * points[k][1] \
                                     + points[k][0] * points[i][1] \
                                     - points[i][1] * points[j][0] \
                                     - points[j][1] * points[k][0] \
                                     - points[k][1] * points[i][0])
                    if area > ret:
                        ret = area
        return ret

# easy: https://www.lintcode.com/problem/largest-triangle-area/
