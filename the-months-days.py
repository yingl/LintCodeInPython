class Solution:
    """
    @param year: a number year
    @param month: a number month
    @return: Given the year and the month, return the number of days of the month.
    """
    def getTheMonthDays(self, year, month):
        # write your code here
        if month == 2:
            return 29 if self.is_leap_year(year) else 28
        else:
            return 31 if month in [1, 3, 5, 7, 8, 10, 12] else 30
        
    def is_leap_year(self, year):
        return (((year % 4) == 0) and ((year % 100) != 0)) or ((year % 400) == 0)

# easy: https://www.lintcode.com/problem/the-months-days/
