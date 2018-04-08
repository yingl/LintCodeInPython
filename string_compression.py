class Solution:
    """
    @param str: a string
    @return: a compressed string
    """
    def compress(self, str):
        # write your code here
        if not str:
            return str
        ret = [str[0]]
        prev_c = str[0]
        count = 1
        for i in range(1, len(str)):
            if str[i] == prev_c:
                count += 1
            else:
                ret.append('%d' % count)
                prev_c = str[i]
                ret.append(prev_c)
                count = 1
        ret.append('%d' % count)
        ret = ''.join(ret)
        return str if len(ret) >= len(str) else ret

# easy: http://lintcode.com/zh-cn/problem/string-compression/
