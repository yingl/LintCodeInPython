class Solution:
    """
    @param s: a string
    @return: the number of substrings
    """
    def countBinarySubstrings(self, s):
        # Write your code here
        ret = 0
        if len(s) > 1:
            i, pre = 0, -1 # -1代表还没开始
            while i < len(s):
                j = i # 记录i原来的值
                while (i < len(s)) and (s[i] == s[j]):
                    i += 1
                _len = i - j # 连续0/1的长度
                if pre != -1: # 上一段0/1的长度已记录
                    ret += min(pre, _len)
                pre = _len # 更新长度
        return ret

# easy: https://www.lintcode.com/problem/count-binary-substrings/
