class Solution:
    """
    @param A: Initial chessboard
    @param F: Flipped coordinates
    @return:  return to the flipped board.
    """
    def ChessPieceRotation(self, A, F):
        # write your code here
        rows, cols = len(A), len(A[0])
        records = [[0 for i in range(cols)] for i in range(rows)]
        for f in F:
            x, y = f[0] - 1, f[1] - 1;
            if (y - 1) >= 0: # 上
                records[x][y - 1] += 1
            if (y + 1) < 4: # 下
                records[x][y + 1] += 1
            if (x - 1) >= 0: # 左右
                records[x - 1][y] += 1
            if (x + 1) < 4: #右
                records[x + 1][y] += 1
        for row in range(rows):
            for col in range(cols):
                if (records[row][col] % 2) != 0:
                    A[row][col] = 1 - A[row][col]
        return A
        
# easy: https://www.lintcode.com/problem/chess-piece-rotation/
