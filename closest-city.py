class Solution:
    """
    @param x: an array of integers, the x coordinates of each city[i]
    @param y: an array of integers, the y coordinates of each city[i]
    @param c: an array of strings that represent the names of each city[i]
    @param q: an array of strings that represent the names of query locations
    @return: the closest city for each query
    """
    def NearestNeighbor(self, x, y, c, q):
        # write your code here
        ret = []
        di_x = {}
        di_y = {}
        di_city = {}
        for i in range(len(c)):
            xi = x[i]
            yi = y[i]
            city = c[i]
            if xi not in di_x:
                di_x[xi] = []
            di_x[xi].append(city)
            if yi not in di_y:
                di_y[yi] = []
            di_y[yi].append(city)
            if city not in di_city:
                di_city[city] = [xi, yi]
        for qcity in q:
            r = None
            dist = 1000000000
            qx = di_city[qcity][0]
            qy = di_city[qcity][1]
            if qx in di_x:
                for c in di_x[qx]:
                    if c != qcity:
                        cy = di_city[c][1]
                        _dist = abs(cy - qy)
                        if _dist < dist:
                            dist = _dist
                            r = c
                        elif _dist == dist:
                            if c < r:
                                r = c
                for c in di_y[qy]:
                    if c != qcity:
                        cx = di_city[c][0]
                        _dist = abs(cx - qx)
                        if _dist < dist:
                            dist = _dist
                            r = c
                        elif _dist == dist:
                            if c < r:
                                r = c
            if not r:
                ret.append('NONE')
            else:
                ret.append(r)
        return ret
        
# easy: https://www.lintcode.com/problem/closest-city/
