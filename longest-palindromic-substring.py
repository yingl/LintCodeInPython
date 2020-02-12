def find_longest_alindrome(s, start, end):
    ret = [0, None, None]
    while (start >= 0) and (end < len(s)):
        if s[start] == s[end]:
            ret[0] = end - start + 1
            ret[1], ret[2] = start, end
            start -= 1
            end += 1
        else:
            break
    return ret
    
class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        # 有O(n)的算法，不过复杂到难以理解，先弃坑了...
        ret = [0, 0, 1]
        for i in range(len(s)):
            r1 = find_longest_alindrome(s, i, i)
            r2 = find_longest_alindrome(s, i, i + 1)
            if r1[0] > ret[0]:
                ret = r1
            if r2[0] > ret[0]:
                ret = r2
        return s[ret[1]:ret[2] + 1]

# medium: https://www.lintcode.com/problem/longest-palindromic-substring/
