class Solution:
    """
    @param s: the given string
    @return: all the possible states of the string after one valid move
    """
    def generatePossibleNextMoves(self, s):
        # write your code here
        ret = []
        for i in range(len(s) - 1):
            flipped = []
            if (s[i] == '+') and (s[i + 1] == '+'):
                if i > 0:
                    flipped.append(s[:i])
                flipped.append('--')
                if (i + 2) < len(s):
                    flipped.append(s[i + 2:])
            if flipped:
                ret.append(''.join(flipped))
        return ret

# easy: https://www.lintcode.com/problem/flip-game/
