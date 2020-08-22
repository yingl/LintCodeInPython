class Solution:
    """
    @param s: A string containing only uppercase and lowercase letters
    @return: Judge whether it can become a palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        di = {}
        odd_chars = 0
        for c in s:
            if c not in di:
                di[c] = 0
            di[c] += 1
        for k, v in di.items():
            if (v % 2) == 1:
                odd_chars += 1
        return odd_chars <= 1
        
# easy: https://www.lintcode.com/problem/pioneering-palindrome/
