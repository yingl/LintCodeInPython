def build_di(s, start, end):
    di = {}
    for i in range(start, end):
        update_di(di, s[i], 'add')
    return di

def update_di(di, key, op='remove'):
    if op == 'remove':
        di[key] -= 1
        if di[key] == 0:
            del di[key]
    else:
        if key in di:
            di[key] += 1
        else:
            di[key] = 1

class Solution:
    """
    @param s: a string
    @param p: a string
    @return: a list of index
    """
    def findAnagrams(self, s, p):
        # write your code here
        ret = []
        len_p = len(p)
        if len(s) < len_p:
            return ret
        di_p = build_di(p, 0, len_p)
        di_s = build_di(s, 0, len_p)
        if di_s == di_p:
            ret.append(0)
        for i in range(1, len(s) - len_p + 1):
            update_di(di_s, s[i - 1], 'remove')
            update_di(di_s, s[i + len_p - 1], 'add')
            if s[i] in di_p:
                if di_p == di_s:
                    ret.append(i)
        return ret

# easy: https://www.lintcode.com/problem/find-all-anagrams-in-a-string/
