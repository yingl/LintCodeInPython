class Solution:
    """
    @param words: a list of strings
    @return: the longest word in words that can be built one character at a time by other words in words
    """
    def longestWord(self, words):
        # Write your code here
        ret = [-1, None]
        s = set(words)
        for word in words:
            i = len(word)
            while i > 0:
                if word[:i] not in s:
                    break
                i -= 1
            if i == 0:
                if len(word) > ret[0]:
                    ret = [len(word), word]
                elif len(word) == ret[0]:
                    if word < ret[1]:
                        ret[1] = word
        return ret[1]

# easy: https://www.lintcode.com/problem/longest-word-in-dictionary/
