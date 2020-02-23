class Solution:
    """
    @param words: the given list of words
    @return: the number of different transformations among all words we have
    """
    def uniqueMorseRepresentations(self, words):
        # Write your code here
        table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        s = set([])
        for word in words:
            codes = []
            for c in word:
                codes += table[ord(c) - ord('a')]
            morsed = ''.join(codes)
            if morsed not in s:
                s.add(morsed)
        return len(s)

# easy: https://www.lintcode.com/problem/unique-morse-code-words/
