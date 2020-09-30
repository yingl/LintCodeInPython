class Solution:
    """
    @param carrot: an integer matrix
    @return: Return the number of steps that can be moved.
    """
    def PickCarrots(self, carrot):
        # write your code here
        rows = len(carrot)
        cols = len(carrot[0])
        cr = int((rows -1) / 2)
        cc = int((cols -1) / 2)
        marked = [[False] * cols for i in range(rows)]
        ret = carrot[cr][cc]
        marked[cr][cc] = True
        r, c = cr, cc
        while True:
            dirs = [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]] # 上下左右
            nums = [-1, -1, -1, -1]
            pos = 0
            for i in range(len(dirs)):
                _r = dirs[i][0]
                _c = dirs[i][1]
                if ((_r >= 0) and (_r < rows)) and ((_c >= 0) and (_c < cols)) and (not marked[_r][_c]):
                    nums[i] = carrot[_r][_c]
                if nums[i] >= nums[pos]:
                    pos = i
            if nums[pos] == -1:
                break
            r = dirs[pos][0]
            c = dirs[pos][1]
            if marked[r][c]:
                break
            ret += carrot[r][c]
            marked[r][c] = True
        return ret 

# easy: https://www.lintcode.com/problem/pick-carrots/
