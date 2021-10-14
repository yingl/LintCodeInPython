class Solution:
    """
    @param str: the origin string
    @return: the start and end of every twitch words
    """
    def twitchWords(self, str):
        # Write your code here
        r = []
        i = 0
        prev = None
        c = 0
        p = 0
        while i < len(str):
            if str[i] != prev:
                if c >= 3:
                    r.append([p, p + c - 1])
                prev = str[i]
                c = 1
                p = i
            else:
                c += 1
            i += 1
        if c >= 3:
            r.append([p, p + c - 1])
        return r

# easy: https://www.lintcode.com/problem/1401/
