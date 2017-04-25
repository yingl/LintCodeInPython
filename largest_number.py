# coding: utf-8

class Solution: 
    #@param num: A list of non negative integers
    #@return: A string
    def largestNumber(self, num):
        # write your code here
        if not num:
            return 0
        for i in xrange(len(num)):
            for j in xrange(len(num) - 1):
                x, y = num[j], num[j + 1]
                x10 = self.log10(x)
                y10 = self.log10(y)
                # 这步是关键，log判断不同位数的大小，log后做加法处理位数相同的情况。
                if x * pow(10, y10) + y < y * pow(10, x10) + x:
                    num[j], num[j + 1] = y, x
        ret = ''
        for n in num:
            if (n != 0) or (ret != '0'):
                ret += str(n)
        return ret

    def log10(self, x):
        ret = 0
        while x > 0:
            x /= 10
            ret += 1
        return ret

# medium: http://lintcode.com/zh-cn/problem/largest-number/
