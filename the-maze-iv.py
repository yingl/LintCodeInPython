class Solution:
    """
    @param maps: 
    @return: 
    """
    def the_maze_i_v(self, maps):
        # 
        ret = 0
        md = 0
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        paths = [set(), set()]
        curr = 0
        rows, cols = len(maps), len(maps[0])
        for i in range(rows):
            for j in range(cols):
                if maps[i][j] == 'S':
                    paths[curr].add((i, j))
        while paths[curr]:
            if ret == 32:
                k = 0
                for i in range(rows):
                    for j in range(cols):
                        if maps[i][j] == '.':
                            k += 1
            for p in paths[curr]:
                if maps[p[0]][p[1]] == 'T':
                    return ret
                for d in dirs:
                    r = p[0] + d[0]
                    c = p[1] + d[1]
                    if (r >= 0) and (r < rows) and (c >= 0) and (c < cols) and ((maps[r][c] == '.') or (maps[r][c] == 'T')):
                        paths[1 - curr].add((r, c))
                maps[p[0]][p[1]] = '#'
            paths[curr].clear()
            curr = 1 - curr
            ret += 1
        return -1
      
# medium: https://www.lintcode.com/problem/1685/
