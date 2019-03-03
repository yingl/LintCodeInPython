class Solution:
    """
    @param version1: the first given number
    @param version2: the second given number
    @return: the result of comparing
    """
    def compareVersion(self, version1, version2):
        # Write your code here
        v1s = version1.split('.') # 先分隔字符串，如果不用python还是建议直接扫字符串比较。
        v2s = version2.split('.')
        v1s = [int(v) for v in v1s]
        v2s = [int(v) for v in v2s]
        for i in range(min(len(v1s), len(v2s))): # 以短的为基准，如果长度一样，那么长得赢了。
            if v1s[i] < v2s[i]:
                return -1
            elif v1s[i] > v2s[i]:
                return 1
        if len(v1s) == len(v2s):
            return 0
        elif len(v1s) > len(v2s):
            return 1
        else:
            return -1

# medium: https://www.lintcode.com/problem/compare-version-numbers
