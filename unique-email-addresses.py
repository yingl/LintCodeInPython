class Solution:
    """
    @param emails: 
    @return: The number of the different email addresses
    """
    def numUniqueEmails(self, emails):
        # write your code here
        r = set([])
        for e in emails:
            ls, rs = e.split('@')
            ls = ls.split('+')[0]
            ls = ls.replace('.', '')
            r.add(ls + '@' + rs)
        return len(r)

# easy: https://www.lintcode.com/problem/1713/
