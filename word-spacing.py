class Solution:
    """
    @param words: the words given.
    @param wordA: the first word you need to find.
    @param wordB: the second word you need to find.
    @return: return the spacing of the closest wordA and wordB.
    """
    def wordSpacing(self, words, wordA, wordB):
        # write your code here.
        ret = len(words)
        ais = []
        bis = []
        for i in range(len(words)):
            word = words[i]
            if word == wordA:
                ais.append(i)
            elif word == wordB:
                bis.append(i)
        if (not ais) or (not bis):
            return -1
        for i in ais:
            for j in bis:
                dist = abs(j - i)
                if dist < ret:
                    ret = dist
        return ret
        
# easy: https://www.lintcode.com/problem/word-spacing/
