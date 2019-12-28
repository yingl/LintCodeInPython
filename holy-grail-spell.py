class Solution:
    """
    @param Spell: The Spell
    @return: nothing
    """
    def holyGrailspell(self, Spell):
        # Write your code here
        ret = []
        for i in range(26):
            ret.append([0, 0])
        for c in Spell:
            c = ord(c)
            if (c >= ord('a')) and (c <= ord('z')):
                ret[c - ord('a')][0] = 1
            else:
                ret[c - ord('A')][1] = 1
        for i in range(25, -1, -1):
            if ret[i] == [1, 1]:
                return chr(i + ord('A'))

# easy: https://www.lintcode.com/problem/holy-grail-spell/
