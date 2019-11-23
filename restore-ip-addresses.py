# coding: utf-8

class Solution:
    # @param {string} s the IP string
    # @return {string[]} All possible valid IP addresses
    def restoreIpAddresses(self, s):
        # Write your code here
        self.ret = []
        self.dfs([], s, 0, len(s), 0)
        return self.ret
                
    def dfs(self, ip, s, start, end, part):
        if (start == len(s)) and (part == 4):
            self.ret.append('.'.join(ip))
        elif (start < len(s)) and (part < 4):
            for i in xrange(3):
                if (start + i) < end:
                    n = self.int2str(s, start, start + i + 1)
                    if (n >= 0) and (n <= 255):
                        if (n == 0) and (i > 0):    # 0只能出现1次
                            continue
                        if (n > 0) and (s[start] == '0'):   # 大于0的元素不能0开头
                            continue
                        ip.append(str(n))
                        self.dfs(ip, s, start + i + 1, end, part + 1)
                        ip.pop()
        
    def int2str(self, s, start, end):
        ret = int(s[start])
        for i in xrange(start + 1, end):
            ret = ret * 10 + int(s[i])
        return ret

# medium: http://lintcode.com/zh-cn/problem/restore-ip-addresses/
