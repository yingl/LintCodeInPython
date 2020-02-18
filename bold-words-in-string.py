class Solution:
    """
    @param words: the words
    @param S: the string
    @return: the string with least number of tags
    """
    def boldWords(self, words, S):
        # Write your code here
        ret = []
        bold_mark = [False] * len(S)
        for i in range(len(S)):
            for word in words:
                l = len(word)
                if (i + l) <= len(S):
                    if S[i: i + l] == word:
                        for j in range(i, i + l):
                            bold_mark[j] = True
        is_bold = False
        for i in range(len(S)):
            if bold_mark[i] and (not is_bold):
                ret.append('<b>')
                is_bold = True
            elif (not bold_mark[i]) and is_bold:
                ret.append('</b>')
                is_bold = False
            ret.append(S[i])
        if is_bold:
            ret.append('</b>')
        return ''.join(ret)

# easy: https://www.lintcode.com/problem/bold-words-in-string/
