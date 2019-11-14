# coding: utf-8

class Solution:
    # @param strs: A list of strings
    # @return: The longest common prefix
    def longestCommonPrefix(self, strs):
        # write your code here
        ret = []
        i = 0
        while True:
            ch = None
            for _str in strs:
                if i >= len(_str):
                    ch = None
                    break
                if not ch:
                    ch = _str[i]
                else:
                    if ch != _str[i]:
                        ch = None
                        break
            if ch:
                ret.append(ch)
                i += 1
            else:
                break
        return ''.join(ret)

# medium: http://lintcode.com/zh-cn/problem/longest-common-prefix/
