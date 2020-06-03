class Solution:
    """
    @param a: A number
    @return: Returns the maximum number after insertion
    """
    def InsertFive(self, a):
        # write your code here
        ret = []
        s = list(str(abs(a)))
        inserted = False
        if a < 0:
            ret.append('-')
        for c in s:
            if a >= 0:
                if (int(c) < 5) and (not inserted):
                    ret.append('5')
                    inserted = True
            else:
                if (int(c) > 5) and (not inserted):
                    ret.append('5')
                    inserted = True
            ret.append(c)
        if not inserted:
            ret.append('5')
        return int(''.join(ret))
        
# easy: https://www.lintcode.com/problem/insert-five/
