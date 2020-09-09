class Solution:
    """
    @param position: the position of circle A,B and point P.
    @return: if two circle intersect return 1, otherwise -1.
    """
    def IfIntersect(self, position):
        #
        # 判断两个圆相交：abs(r1 - r2) <= dist <= r1 + r2
        xa = position[0]
        ya = position[1]
        ra = position[2]
        xb = position[3]
        yb = position[4]
        rb = position[5]
        xp = position[6]
        yp = position[7]
        dist_ab = math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)
        dist_bp = math.sqrt((xp - xb) ** 2 + (yp - yb) ** 2)
        min_rab = abs(ra - rb)
        max_rab = ra + rb
        if (min_rab <= dist_ab) and (dist_ab <= max_rab): # 初始相交
            return 1
        elif (min_rab <= dist_bp) and (dist_bp <= max_rab): # P点相交
            return 1
        a = yp - ya # 这里公式都忘了...
        b = xa - xp
        if (a == 0) and (b == 0):
            return -1
        c = xp * ya - xa * yp
        dist = (a * xb + b * yb + c) / math.sqrt(a * a + b * b)
        xi = (b * b * xb - a * b * yb - a * c) / (a * a + b * b)
        yi = (a * a * yb - a * b * xb - b * c) / (a * a + b * b)
        if (min_rab <= dist) and (dist <= max_rab):
            if self.is_inline([xa, ya], [xp, yp], [xi, yi], ra): # 交点是不是在直线上
                return 1
        return -1
        
    def is_inline(self, pa, pp, pb, ra):
        max_x = pa[0] if pa[0] > pp[0] else pp[0]
        min_x = pp[0] if pa[0] > pp[0] else pa[0]
        max_y = pa[1] if pa[1] > pp[1] else pp[1]
        min_y = pp[1] if pa[1] > pp[1] else pa[1]
        flag = ((pb[0] - pa[0]) * (pp[1] - pa[1])) == ((pp[0] - pa[0]) * (pb[1] - pa[1]))
        return flag and ((min_x <= pb[0]) and (pb[0 ]<= max_x)) and ((min_y <= pb[1]) and (pb[1] <= max_y))

# medium: https://www.lintcode.com/problem/moving-circle/
