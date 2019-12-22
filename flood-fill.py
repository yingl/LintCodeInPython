class Solution:
    """
    @param image: a 2-D array
    @param sr: an integer
    @param sc: an integer
    @param newColor: an integer
    @return: the modified image
    """
    def floodFill(self, image, sr, sc, newColor):
        # Write your code here
        self.old_olor = image[sr][sc]
        self._floodFill(image, sr, sc, newColor)
        return image

    def _canGo(self, image, row, col, _dir):
        new_row, new_col = row, col
        if _dir == 0: # Up
            new_row -= 1
        elif _dir == 1: # Down
            new_row += 1
        elif _dir == 2: # Left
            new_col -= 1
        else: # Right
            new_col += 1
        if (new_row >= 0) and (new_row < len(image)) \
           and (new_col >= 0) and (new_col < len(image[0])):
            if image[new_row][new_col] == self.old_olor:
                return (new_row, new_col)
        return None
        
    def _floodFill(self, image, row, col, new_color):
        image[row][col] = new_color
        for _dir in range(4):
            r = self._canGo(image, row, col, _dir)
            if r:
                self._floodFill(image, r[0], r[1], new_color)
                
# easy: https://www.lintcode.com/problem/flood-fill/
