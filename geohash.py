import base64

class GeoHash:
    """
    @param: latitude: one of a location coordinate pair 
    @param: longitude: one of a location coordinate pair 
    @param: precision: an integer between 1 to 12
    @return: a base32 string
    """
    def encode(self, latitude, longitude, precision):
        # write your code here
        l = 5 * precision - 1
        longs, lats = [-180, 180], [-90, 90]
        code = []
        while l >= 0:
            long_mid = (longs[0] + longs[1]) / 2
            lat_mid = (lats[0] + lats[1]) / 2
            if longitude > long_mid:
                code.append(1) 
                longs[0] =long_mid
            else:
                code.append(0)
                longs[1] = long_mid
            if latitude > lat_mid:
                code.append(1) 
                lats[0] = lat_mid
            else:
                code.append(0)
                lats[1] = lat_mid
            l -= 2
        return self.base32(code, precision)
        
    def base32(self, code, precision):
        r = ''
        chars = '0123456789bcdefghjkmnpqrstuvwxyz'
        for i in range(0, precision * 5, 5):
            idx = 0
            for j in range(5):
                idx = idx * 2 + code[i + j]
            r += chars[idx]
        return r
