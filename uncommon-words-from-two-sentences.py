class Solution:
    """
    @param A: Sentence A
    @param B: Sentence B
    @return: Uncommon Words from Two Sentences
    """
    def uncommonFromSentences(self, A, B):
        # Write your code here.
        ret = []
        di_a, di_b = {}, {}
        words_a = A.split(' ')
        words_b = B.split(' ')
        self.buildDict(words_a, di_a)
        self.buildDict(words_b, di_b)
        self.checkWords(di_a, di_b, ret)
        self.checkWords(di_b, di_a, ret)
        return ret

    def buildDict(self, words, di):
        for word in words:
            if word in di:
                di[word] += 1
            else:
                di[word] = 1
                
    def checkWords(self, di_src, di_target, ret):
        for k in di_src:
            if (di_src[k] == 1) and (k not in di_target):
                ret.append(k)

# easy: https://www.lintcode.com/problem/uncommon-words-from-two-sentences/
