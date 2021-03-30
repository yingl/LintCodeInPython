class Solution:
    """
    @param words: the list of word.
    @return: the length of the longest string chain.
    """
    def longestStrChain(self, words):
        #
        di = {}
        for w in words:
            i = len(w)
            if i not in di:
                di[i] = []
            di[i].append(w)
        levels = [[], []]
        curr = 0
        start_len = 1
        l = 1 # 字符串链长度，最小为1。
        while start_len <= 1000: # 根据条件，一定有结果的。
            if start_len in di:
                levels[curr] = di[start_len]
                break
            start_len += 1
        while levels[curr]:
            next_words = []
            if (start_len + l) in di: # 判断能否扩展
                next_words = di[start_len + l]
            for w in levels[curr]:
                for nw in next_words:
                    chars = {}
                    for c in w:
                        if c not in chars:
                            chars[c] = 0
                        chars[c] += 1
                    for c in nw:
                        if c not in chars:
                            chars[c] = 0
                        chars[c] -= 1
                    diff = 0
                    for v in chars.values():
                        diff += abs(v)
                    if diff == 1:
                        levels[curr ^ 1].append(nw)
            levels[curr] = []
            curr ^= 1
            l += 1
        return l - 1
      
# medium: https://www.lintcode.com/problem/longest-string-chain/
