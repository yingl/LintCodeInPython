class Solution:
    """
    @param words: the array of string means the list of words
    @param order: a string indicate the order of letters
    @return: return true or false
    """
    def isAlienSorted(self, words, order):
        #
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        di = {}
        for i in range(len(order)):
            di[order[i]] = alphabets[i]
        new_words = []
        for word in words:
            nw = []
            for c in word:
                nw.append(di[c])
            new_words.append(''.join(nw))
        for i in range(len(new_words) - 1):
            if new_words[i] > new_words[i + 1]:
                return False
        return True

# easy: https://www.lintcode.com/problem/alien-dictionaryeasy/
