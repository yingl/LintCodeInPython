class Solution:
    """
    @param s: a string
    @return: reverse only the vowels of a string
    """
    def reverseVowels(self, s):
        # write your code here
        ret = list(s)
        vs = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        i, j = 0, len(s) - 1
        while i < j:
            while i < len(s):
                if ret[i] in vs:
                    break
                else:
                    i += 1
            while j >= 0:
                if ret[j] in vs:
                    break
                else:
                    j -= 1
            if i < j:
                ret[i], ret[j] = ret[j], ret[i]
            i += 1
            j -= 1
        return ''.join(ret)

# easy: https://www.lintcode.com/problem/reverse-vowels-of-a-string/
