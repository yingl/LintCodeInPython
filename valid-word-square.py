class Solution:
    """
    @param words: a list of string
    @return: a boolean
    """
    def validWordSquare(self, words):
        # Write your code here
        for i in range(len(words)):
            for j in range(len(words[i])):
                try:
                    if words[i][j] != words[j][i]:
                        return False
                except:
                    return False
        return True

# easy: https://www.lintcode.com/problem/valid-word-square/
