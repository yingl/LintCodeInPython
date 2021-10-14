class Solution:
    """
    @param s: the string
    @return: the number of substring
    """
    def countSubstrings(self, s):
        # Write your code here.
        ret = set([])
        for i in range(len(s)):
            l = i
            for j in range(2): # 处理奇数偶数长度
                r = l + j # 0是奇数，1是偶数。
                while (l >= 0) and (r < len(s)) and (s[l] == s[r]):
                    ret.add(s[l : r + 1])
                    l -= 1
                    r += 1
                l = i
        return len(ret)
      
# easy: https://www.lintcode.com/problem/1856/
