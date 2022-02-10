class Solution:
    """
    @param S: a String consists of a and b
    @return: the longest of the longest string that meets the condition
    """
    def getAns(self, S):
        # Write your code here
        r = 0
        diff = 0
        diffs = []
        pos = {}
        for i in range(len(S)):
            if S[i] == 'A':
                diff += 1
            else:
                diff -= 1
            diffs.append(diff)
            pos[diff] = i
        for i in range(len(S)):
            if diffs[i] != 0:
                if r <= pos[diffs[i]] - i:
                    r = pos[diffs[i]] - i
        if 0 in pos:
            if (pos[0] + 1) > r:
                r = pos[0] + 1
        return r
