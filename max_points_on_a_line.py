# coding: utf-8

class Solution:
    # @param {int[]} points an array of point
    # @return {int} an integer
    def maxPoints(self, points):
        # Write your code here
        ret = 0
        if points:
            for i in xrange(len(points)):
                slopes = {}
                for j in xrange(len(points)):
                    if i != j:
                        slope = self.calcSlope(points[i], points[j])
                        if slope not in slopes:
                            slopes[slope] = 2 # 第一次要记录两个点
                        else:
                            slopes[slope] += 1
                for slope, count in slopes.items():
                    if count > ret:
                        ret = count
            if ret == 0:
                ret = 1
        return ret

    def calcSlope(self, point_x, point_y):
        if point_x.x == point_y.x:
            return 2147483647
        else: # 如果浮点数不能解决问题就用最大公约数！
            return float(point_x.y - point_y.y) / float(point_x.x - point_y.x)

# medium: http://lintcode.com/zh-cn/problem/max-points-on-a-line/
