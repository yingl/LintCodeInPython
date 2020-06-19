class Solution:
    """
    @param words: a list of strings
    @return: return a list of strings
    """
    def findWords(self, words):
        # write your code here
        ret = []
        di = {'Q': 1, 'W': 1, 'E': 1, 'R': 1, 'T': 1, 'Y': 1, 'U': 1, 'I': 1, 'O': 1, 'P': 1,
              'A': 2, 'S': 2, 'D': 2, 'F': 2, 'G': 2, 'H': 2, 'J': 2, 'K': 2, 'L': 2,
              'Z': 3, 'X': 3, 'C': 3, 'V': 3, 'B': 3, 'N': 3, 'M': 3}
        for word in words:
            line = None
            match = True
            for c in word.upper():
                if not line:
                    line = di[c]
                else:
                    if line != di[c]:
                        match = False
                        break
            if match:
                ret.append(word)
        return ret
                        
# easy: https://www.lintcode.com/problem/keyboard-row/
