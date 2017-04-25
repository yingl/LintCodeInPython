# coding: utf-8

class StringUtils:
    # @param {string} originalStr the string we want to append to
    # @param {int} size the target length of the string
    # @param {string} padChar the character to pad to the left side of the string
    # @return {string} a string
    @classmethod
    def leftPad(self, originalStr, size, padChar=' '):
        # Write your code here
        result = ''
        dist = size - len(originalStr)
        if dist > 0:
            for i in xrange(dist):
                result += padChar
            return result + originalStr
        else:
            return originalStr

# easy: http://lintcode.com/zh-cn/problem/left-pad/
