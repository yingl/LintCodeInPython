class Solution:
    """
    @param words: a list of words
    @param word1: a string
    @param word2: a string
    @return: the shortest distance between word1 and word2 in the list
    """
    def shortestDistance(self, words, word1, word2):
        # Write your code here
        ret = len(words)
        i_1, i_2 = -1, -1
        for i in range(len(words)):
            if words[i] == word1:
                i_1 = i
            elif words[i] == word2:
                i_2 = i
            else:
                continue
            if (i_1 >= 0) and (i_2 >= 0):
                print(i_1, i_2)
                ret = min(ret, abs(i_1 - i_2))
        return ret

# easy: https://www.lintcode.com/problem/shortest-word-distance/
