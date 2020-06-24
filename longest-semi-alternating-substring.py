class Solution:
    """
    @param s: the string
    @return: length of longest semi alternating substring
    """
    def longestSemiAlternatingSubstring(self, s):
        # write your code here
        if not s:
            return 0
        ret = []
        count = 1
        s += ' ' # 方便处理结束位置
        ss = s[0] # 初始化子串第一个字符
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                if count >= 3:
                    j = count - 2 # ???
                    ret.append(len(ss[:-j])) #因为之前重复次数会大于3，所以重复的字最多保留2个。
                    ss = s[i - 1] * 2 # 重新初始ss，也就是最近的两个重复字符开始。
                elif s[i] == ' ':
                    ret.append(len(ss))
                count = 1 # 重新计数
            else:
                count += 1 # 更新连续出现字符长度
            ss += s[i]
        return max(ret)
        
# easy: https://www.lintcode.com/problem/longest-semi-alternating-substring/
