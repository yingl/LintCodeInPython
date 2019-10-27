class Solution:
    """
    @param paragraph: 
    @param banned: 
    @return: nothing
    """
    def mostCommonWord(self, paragraph, banned):
        di = {}
        banned_s = set([])
        for b in banned:
            banned_s.add(b.lower())
        word = []
        for c in paragraph:
            if c in [' ', ',', '.', '!', '?', ';', "'"]:
                if word:
                    w = ''.join(word).lower()
                    if w not in banned_s:
                        if w in di:
                            di[w] += 1
                        else:
                            di[w] = 1
                    word = []
            else:
                word.append(c)
        if word:
            w = ''.join(word).lower()
            if w not in banned_s:
                if w in di:
                    di[w] += 1
                else:
                    di[w] = 1
        ret, c = None, 0
        for k, v in di.items():
            if v > c:
                c = v
                ret = k
        return ret
        
# easy: https://www.lintcode.com/problem/most-common-word/
