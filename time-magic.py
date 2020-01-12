class Solution:
    """
    @param newTime: new time
    @return: maximum time
    """
    def timeMagic(self, newTime):
        #
        h, m = newTime.split(':')
        h = list(h)
        m = list(m)
        h_index, m_index = -1, -1
        if (h[0] == '?') and (h[1] == '?'):
            h = ['2', '3']
        else:
            if h[0] == '?':
                h_index = 0
            elif h[1] == '?':
                h_index = 1
        if (m[0] == '?') and (m[1] == '?'):
            m = ['5', '9']
        else:
            if m[0] == '?':
                m_index = 0
            elif m[1] == '?':
                m_index = 1
        if h_index != -1:
            for i in range(9, 0, -1):
                h[h_index] = str(i)
                if self.validate(int(h[0]) * 10 + int(h[1]), 'h'):
                    break
        if m_index != -1:
            for i in range(9, 0, -1):
                m[m_index] = str(i)
                if self.validate(int(m[0]) * 10 + int(m[1]), 'm'):
                    break
        return ':'.join([''.join(h), ''.join(m)])
        
    def validate(self, val, part):
        if part == 'h':
            return (val >= 0) and (val <= 23)
        else:
            return (val >= 0) and (val <= 59)
            
# easy: https://www.lintcode.com/problem/time-magic/
