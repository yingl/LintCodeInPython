class Solution:
    """
    @param sourceString: a string
    @param targetStrings: a string array
    @return: Returns a bool array indicating whether each string in targetStrings is a substring of the sourceString
    """
    def whetherStringsAreSubstrings(self, sourceString, targetStrings):
        # write your code here
        ret = []
        di = {}
        for i in range(len(sourceString)):
            c = sourceString[i]
            if c not in di:
                di[c] = []
            di[c].append(i)
        for s in targetStrings:
            if s:
                c = s[0]
                if c not in di:
                    ret.append(False)
                else:
                    match = False
                    for start in di[c]:
                        r = True
                        for i in range(len(s)):
                            if (start + i) < len(sourceString):
                                if s[i] != sourceString[i + start]:
                                    r = False
                                    break
                            else:
                                r = False
                                break
                        if r:
                            match = True
                            break
                    ret.append(match)
            else:
                ret.append(True)
        return ret

# easy: https://www.lintcode.com/problem/multi-string-search/
