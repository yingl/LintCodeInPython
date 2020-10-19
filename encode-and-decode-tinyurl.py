class Solution:
    def __init__(self):
        self.i = 0
        self.dict = {}
        self.chars = []
        digits = '0123456789'
        chars = 'abcdefghijklmnopqrstuvwxyz'
        for c in digits:
            self.chars.append(c)
        for c in chars:
            self.chars.append(c)
        for c in chars.upper():
            self.chars.append(c)
    def encode(self, longUrl):
        # Encodes a URL to a shortened URL.
        hval = self.hash(longUrl)
        llen = len(self.chars)
        code = []
        while (hval != 0):
            code.append(self.chars[hval % llen])
            hval = int(hval / llen)
        code = ''.join(code)
        self.dict[code] = longUrl
        return 'http://tinyurl.com/' + code        

    def decode(self, shortUrl):
        # Decodes a shortened URL to its original URL.
        code = shortUrl.split('/')[-1]
        return self.dict[code]
        
    def hash(self, s):
        ret = 0
        for c in s:
            i = ord(c)
            ret = ret * 33 + i
        return ret % 18446744073709551616 # 2 ** 64

# Your Codec object will be instantiated and called as such:
# Codec codec = new Codec();
# codec.decode(codec.encode(url));

# medium: https://www.lintcode.com/problem/encode-and-decode-tinyurl/
