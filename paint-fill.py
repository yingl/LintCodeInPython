class Solution:
    """
    @param screen: a two-dimensional array of colors
    @param x: the abscissa of the specified point
    @param y: the ordinate of the specified point
    @param newColor: the specified color
    @return: Can it be filled
    """
    def paintFill(self, screen, x, y, newColor):
        # write your code here.
        if screen[x][y] == newColor:
            return False
        old_color = screen[x][y]
        screen[x][y] = newColor
        if x > 0: # Left
            if screen[x - 1][y] == old_color:
                self.paintFill(screen, x - 1, y, newColor)
        elif x < (len(screen[0]) - 1): # Right
            if screen[x + 1][y] == old_color:
                self.paintFill(screen, x + 1, y, newColor)
        elif y > 0: # Up
            if screen[x][y - 1] == old_color:
                self.paintFill(screen, x, y - 1, newColor)
        elif y < (len(screen) - 1):
            if screen[x][y + 1] == old_color:
                self.paintFill(screen, x, y + 1, newColor)
        return True

# easy: https://www.lintcode.com/problem/paint-fill/
