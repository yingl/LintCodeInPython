"""
Definition of Column:
class Column:
    def __init__(self, key, value):
        self.key = key
        self.value = value
"""


class MiniCassandra:
    def __init__(self):
        # do intialization if necessary
        self.di = {}

    """
    @param: row_key: a string
    @param: column_key: An integer
    @param: value: a string
    @return: nothing
    """
    def insert(self, row_key, column_key, value):
        # write your code here
        if row_key not in self.di:
            self.di[row_key] = []
        i = 0
        while i < len(self.di[row_key]): # No TreeMap, use this ugly way!
            if self.di[row_key][i][0] == column_key:
                self.di[row_key][i] = (column_key, value)
                break
            i += 1
        if i == len(self.di[row_key]):
            self.di[row_key].append((column_key, value))
        self.di[row_key].sort()

    """
    @param: row_key: a string
    @param: column_start: An integer
    @param: column_end: An integer
    @return: a list of Columns
    """
    def query(self, row_key, column_start, column_end):
        # write your code here
        r = []
        if row_key in self.di:
            for v in self.di[row_key]:
                if (v[0] >= column_start) and (v[0] <= column_end):
                    r.append('(' + str(v[0]) + ', "' + v[1] + '")')
        return r
