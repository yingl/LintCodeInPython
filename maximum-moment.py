class Solution:
    """
    @param time: a string of Time
    @return: The MaximumMoment
    """
    def MaximumMoment(self, time: str) -> str:
        # Write your code here.
        r = list(time)
        if r[4] == '?':
            r[4] = '9'
        if r[3] == '?':
            r[3] = '5'
        if r[0] == '?':
            if (r[1] == '?') or (r[1] <= '3'):
                r[0] = '2'
            else:
                r[0] = '1'
        if r[1] == '?':
            if (r[0] == '0') or(r[0] == '1'):
                r[1] = '9'
            if r[0] == '2':
                r[1] = '3'
        return ''.join(r)
      
# easy: https://www.lintcode.com/problem/1871/
