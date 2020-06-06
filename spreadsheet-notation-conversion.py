class Solution:
    """
    @param index: the index to be converted
    @return: return the string after convert.
    """
    def convert(self, index):
        # write your code here
        ret = ''
        line = int((index - 1) / 702) + 1
        no = index - (line - 1) * 702
        ret += str(line)
        if no == 702:
            ret += 'Z'
        elif no > 26:
            ret += chr(ord('A') + int(no / 26) - 1)
        ret += chr(ord('A') + (no - 1) % 26)
        return ret
        
# easy: https://www.lintcode.com/problem/spreadsheet-notation-conversion/
