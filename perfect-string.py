class Solution:
    """
    @param s: string need to be transformed
    @param k: minimum char can be transformed in one operation
    @return: minimum times to transform all char into '1'
    """
    def perfectString(self, s, k):
        # Write your code here
        ret = 0
        cz = k # 技巧！
        for c in s:
            if c == '0':
                if cz == k:
                    ret += 1 # 遇到0就替换，后面连着的0尽可能多的一起替换。
                cz -= 1
            else:
                cz = k # 重置
            if cz == 0: # 最多替换k个0
                cz = k
        return ret
        
# easy: https://www.lintcode.com/problem/perfect-string/
