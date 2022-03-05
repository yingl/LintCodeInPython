from typing import (
    List,
)

class Solution:
    """
    @param a: the csv file a
    @return: return the processed file
    """
    def processing_file(self, a: List[str]) -> List[str]:
        # Write your code here
        ret = []
        rows = len(a)
        ls = []
        for i in range(rows):
            words = a[i].split(',')
            for i in range(len(words)):
                if i >= len(ls):
                    ls.append(len(words[i]))
                if len(words[i]) > ls[i]:
                    ls[i] = len(words[i])
        for i in range(rows):
            s = []
            words = a[i].split(',')
            for i in range(len(words)):
                w = words[i]
                s.append(' ' * (ls[i] - len(w)) + w)
            ret.append(','.join(s))
        return ret
      
# medium: https://www.lintcode.com/problem/1618/
