class GeoHash:
    """
    @param: geohash: geohash a base32 string
    @return: latitude and longitude a location coordinate pair
    """
    def decode(self, geohash):
        # write your code here
        code = self.b32decode(geohash)
        longs, lats = [-180, 180], [-90, 90]
        longtitude, latitude = 0, 0
        prec = len(code)
        for i in range(0, prec, 2):
            if code[i] == '0':
                longs[1] = longtitude
            else:
                longs[0] = longtitude
            longtitude = (longs[0] + longs[1]) / 2
            if (i + 1) >= prec:
                break
            if code[i + 1] == '0':
                lats[1] = latitude
            else:
                lats[0] = latitude
            latitude = (lats[0] + lats[1]) / 2
        return (latitude, longtitude)

    def b32decode(self, geohash):
        r = ''
        bcode = {'0': '00000', '1': '00001', '2': '00010', '3': '00011',
                 '4': '00100', '5': '00101', '6': '00110', '7': '00111',
                 '8': '01000', '9': '01001', 'b': '01010', 'c': '01011',
                 'd': '01100', 'e': '01101', 'f': '01110', 'g': '01111',
                 'h': '10000', 'j': '10001', 'k': '10010', 'm': '10011',
                 'n': '10100', 'p': '10101', 'q': '10110', 'r': '10111',
                 's': '11000', 't': '11001', 'u': '11010', 'v': '11011',
                 'w': '11100', 'x': '11101', 'y': '11110', 'z': '11111'}
        for c in geohash:
            r += bcode[c]
        return r
