"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        # Write your code here
        if intervals:
            intervals.sort(key=lambda i: i.start)
            for i in range(len(intervals) - 1):
                if intervals[i + 1].start < intervals[i].end:
                    return False
        return True
        
# easy: https://www.lintcode.com/problem/meeting-rooms/
