class Solution:
    """
    @param s: a string
    @return: reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order
    """
    def reverseWords(self, s):
        # Write your code here
        s = list(s)
        is_word = False
        start, end = -1, -1
        for i in range(len(s)):
            if s[i] != ' ':
                if not is_word:
                    is_word = True
                    start, end = i, i
                else:
                    end += 1
            else:
                is_word = False
                self.reverseWord(s, start, end)
        if is_word:
            self.reverseWord(s, start, end)
        return ''.join(s)
    
    def reverseWord(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

# easy: https://www.lintcode.com/problem/reverse-words-in-a-string-iii/
