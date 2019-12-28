class Solution:
    """
    @param word: a string
    @return: return a boolean
    """
    def detectCapitalUse(self, word):
        # write your code here
        if word[0] == word[0].upper(): # 偷懒了...
            return (word[1:] == word[1:].lower()) \
                   or (word[1:] == word[1:].upper())
        else:
            return word[1:] == word[1:].lower()

# easy: https://www.lintcode.com/problem/detect-capital/
