class Solution:
    """
    @param str: the string
    @param dict: the dictionary
    @return: return words which  are subsequences of the string
    """
    def findWords(self, _str, _dict):
        # Write your code here.
        # same as #23 https://www.lintcode.com/problem/substring-in-dict/
        ret = []
        di = {}
        for i in range(len(_str)):
            if _str[i] in di:
                di[_str[i]].append(i)
            else:
                di[_str[i]] = [i]
        for word in _dict:
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

# medium: https://www.lintcode.com/problem/find-words/
