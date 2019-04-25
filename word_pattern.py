class Solution:
    """
    @param pattern: a string, denote pattern string
    @param teststr: a string, denote matching string
    @return: an boolean, denote whether the pattern string and the matching string match or not
    """
    def wordPattern(self, pattern, teststr):
        # write your code here
        di = {}
        pattern_mapping = []
        _id = 0
        for c in pattern:
            if c not in di:
                di[c] = _id
                _id += 1
            pattern_mapping.append(di[c])
        _id = 0
        di.clear()
        str_mapping = []
        words = teststr.split(' ')
        for word in words:
            if word not in di:
                di[word] = _id
                _id += 1
            str_mapping.append(di[word])
        return str_mapping == pattern_mapping

# easy: https://www.lintcode.com/problem/word-pattern/
