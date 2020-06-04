class Solution:
    """
    @param record: Attendance record.
    @return: If the student should be punished return true, else return false. 
    """
    def judge(self, record):
        # Write your code here.
        cd, cl = 0, 0
        pl = None
        for c in record:
            if c == 'D':
                cd += 1
                if cd == 2:
                    return True
                pl = None
                cl = 0
            elif c == 'L':
                if pl != 'L':
                    pl = 'L'
                    cl += 1
                else:
                    cl += 1
                    if cl == 3:
                        return True
            else:
                pl = None
                cl = 0
        return False

# easy: https://www.lintcode.com/problem/attendance-judgment/
