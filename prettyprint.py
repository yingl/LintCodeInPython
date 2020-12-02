class Solution:
    """
    @param text: the text to print
    @param width: the width of the window
    @return: return the result of pretty print.
    """
    def prettyPrint(self, text, width):
        # write your code here
        ret = ['*' * (width + 2)]
        for line in text:
            n = width
            _line = []
            for word in line:
                if n >= (len(word) + 1):
                    _line.append(word)
                    n -= (len(word) + 1)
                else:
                    if n == len(word):
                        _line.append(word)
                        fmt_line = ' '.join(_line)
                        ret.append('*' + fmt_line + ' ' * (width - len(fmt_line)) + '*')
                        _line = []
                        n = width
                    else:
                        fmt_line = ' '.join(_line)
                        ret.append('*' + fmt_line + ' ' * (width - len(fmt_line)) + '*')
                        _line = [word]
                        n = width - (len(word) + 1)
            if _line:
                fmt_line = ' '.join(_line)
                ret.append('*' + fmt_line + ' ' * (width - len(fmt_line)) + '*')
        ret.append('*' * (width + 2))
        return ret
        
# easy: https://www.lintcode.com/problem/prettyprint/
