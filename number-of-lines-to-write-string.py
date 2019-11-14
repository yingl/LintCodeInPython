class Solution:
    """
    @param widths: an array
    @param S: a string
    @return: how many lines have at least one character from S, and what is the width used by the last such line
    """
    def numberOfLines(self, widths, S):
        # Write your code here
        lines = 0
        steps = 0
        w = 0
        for c in S:
            c = ord(c) - ord('a')
            if w + widths[c] > 100:
                lines += 1
                w = widths[c]
            else:
                w += widths[c]
            steps = w
        return [lines + 1, steps]

# easy: https://www.lintcode.com/problem/number-of-lines-to-write-string/
