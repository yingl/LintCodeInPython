class Solution:
    """
    @param s: a string
    @param wordDict: A set of words.
    @return: All correct words
    """
    def wordSubsequence(self, s, wordDict):
        # write your code here
        # 记录每个字母在哪些位置出现过，
        # 如果位置能构造递增序列则满足。
        ret = []
        di = {}
        for i in range(len(s)):
            if s[i] in di:
                di[s[i]].append(i)
            else:
                di[s[i]] = [i]
        for word in wordDict:
            min_pos = -1
            match = True
            for c in word:
                if c not in di:
                    match = False
                    break
                i = 0
                while i < len(di[c]):
                    if di[c][i] > min_pos:
                        min_pos = di[c][i]
                        break
                    else:
                        i += 1
                if i == len(di[c]): # 没有找到一个位置符合递增条件
                    match = False
                    break
            if match:
                ret.append(word)
        return ret

# medium: https://www.lintcode.com/problem/substring-in-dict/
