class Solution:
    """
    @param n: non-negative integer n.
    @return: return whether a binary representation of a non-negative integer n is a palindrome.
    """
    def isPalindrome(self, n):
        # Write your code here
        num = bin(n)[2:]
        for i in range(len(num)):
            if num[i] != num[-i - 1]:
                return False
        return True

# easy: https://www.lintcode.com/problem/807
