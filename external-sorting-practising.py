class Solution:
    """
    @param files: some files with integers need to be sorted
    @param result: a file for writing numbers
    @param n: numbers of files
    @return: nothing
    """
    def sortOnDisk(self, files, result):
        # write your code here
        # Lazy mode!
        r = []
        for f in files:
            while not f.is_empty():
                r.append(f.read())
        r.sort()
        for i in r:
            result.write(i)
            
# easy: https://www.lintcode.com/problem/351
