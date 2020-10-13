class Solution:
    """
    @param lines: the text to compress.
    @return: return the text after compression.
    """
    def textCompression(self, lines):
        # write your code here.
        ret = []
        di = {}
        i = 1
        for line in lines:
            _ret = []
            word = ''
            for c in line:
                if ((c >= 'a') and (c <= 'z')) or ((c >= 'A') and (c <= 'Z')):
                    word += c
                else:
                    if word:
                        if word in di:
                            _ret.append(str(di[word]))
                        else:
                            _ret.append(word)
                            di[word] = i
                            i += 1
                        word = ''
                    _ret.append(c)
            if word: # 只有一个单词
                if word in di:
                    _ret.append(str(di[word]))
                else:
                    _ret.append(word)
                    di[word] = i
                    i += 1
                word = ''
            ret.append(''.join(_ret))
        return ret
                
# easy: https://www.lintcode.com/problem/text-compression/
