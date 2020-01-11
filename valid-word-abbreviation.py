class Solution:
    """
    @param word: a non-empty string
    @param abbr: an abbreviation
    @return: true if string matches with the given abbr or false
    """
    def validWordAbbreviation(self, word, abbr):
        # write your code here
        word_len = len(word)
        if len(abbr) > len(word):
            return False
        pos = 0
        step = 0
        for c in abbr:
            # print(c)
            if c not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                pos += step
                if c != word[pos]:
                    return False
                pos += 1
                step = 0
            else:
                step = step * 10 + int(c)
                if (pos + step) > len(word):
                    return False
        return True

# easy: https://www.lintcode.com/problem/valid-word-abbreviation/
