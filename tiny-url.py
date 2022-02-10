class TinyUrl:
    def __init__(self):
        self.l2s = {} # long 2 short
        self.s2l = {} # short 2 long
        self.used = 0

    """
    @param: url: a long url
    @return: a short url starts with http://tiny.url/
    """
    def longToShort(self, url):
        # write your code here
        if url in self.l2s:
            return self.l2s[url]
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        surl = 'http://tiny.url/'
        _used = self.used
        for i in range(6):
            surl += chars[_used % 52]
            _used = int(_used / 52)
        self.used += 1
        self.s2l[surl] = url
        return surl


    """
    @param: url: a short url starts with http://tiny.url/
    @return: a long url
    """
    def shortToLong(self, url):
        # write your code here
        return self.s2l[url]
