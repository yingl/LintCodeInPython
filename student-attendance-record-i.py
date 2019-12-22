class Solution:
    """
    @param s: a string
    @return: whether the student could be rewarded according to his attendance record
    """
    def checkRecord(self, s):
        # Write your code here
        prev = None
        count_l, count_a = 0, 0
        for c in s:
            if c == 'L':
                if prev != 'L':
                    count_l = 1
                else:
                    count_l += 1
                if count_l == 3:
                    return False
            else:
                count_l = 0
                if c == 'A':
                    count_a += 1
                    if count_a > 1:
                        return False
            prev = c
        return True

# easy: https://www.lintcode.com/problem/student-attendance-record-i/
