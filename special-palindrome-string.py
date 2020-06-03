class Solution:
    """
    @param ambigram: A list of paired ambigram letter.
    @param word: A string need to be judged.
    @return: If it is special palindrome string, return true.
    """
    def ispalindrome(self, ambigram, word):
        # write your code here.
        di = {}
        for a in ambigram:
            if a[0] not in di:
                di[a[0]] = set([a[0]])
            di[a[0]].add(a[1])
            if a[1] not in di:
                di[a[1]] = set([a[1]])
            di[a[1]].add(a[0])
        for c in word:
            if c not in di:
                di[c] = set([c])
        i, j = 0, len(word) - 1
        while i < j:
            if word[i] != word[j]:
                if not di[word[i]].intersection(di[word[j]]):
                    return False
            i += 1
            j -= 1
        return True
        
# easy: https://www.lintcode.com/problem/special-palindrome-string/
