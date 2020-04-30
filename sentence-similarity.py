class Solution:
    """
    @param words1: a list of string
    @param words2: a list of string
    @param pairs: a list of string pairs
    @return: return a boolean, denote whether two sentences are similar or not
    """
    def isSentenceSimilarity(self, words1, words2, pairs):
        # write your code here
        if len(words1) == len(words2):
            new_pairs = set([])
            for pair in pairs:
                new_pairs.add(pair[0] + pair[1])
                new_pairs.add(pair[1] + pair[0])
            print(new_pairs)
            for i in range(len(words1)):
                same = (words1[i] == words2[i])
                same = same or ((words1[i] + words2[i]) in new_pairs)
                if not same:
                    return False
            return True
        return False
        
# easy: https://www.lintcode.com/problem/sentence-similarity/
