from typing import (
    List,
)

class Solution:
    """
    @param Mine_map: an matrix represents the map.
    @param Start: the start position.
    @return: return an array including all reachable positions.
    """
    def Mine_sweeping(self, Mine_map: List[List[int]], Start: List[int]) -> List[List[int]]:
        # write your code here
        ret = []
        visited = set([])
        cords = [Start]
        xlim, ylim = len(Mine_map), len(Mine_map[0])
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]] # Up, Down, Left, Right
        while cords:
            cord = cords.pop()
            c = cord[0] * 1000 + cord[1]
            if c not in visited:
                visited.add(c)
            if Mine_map[cord[0]][cord[1]] == 0:
                continue
            for d in dirs:
                x, y = cord[0] + d[0], cord[1] + d[1]
                if (x >= 0) and (x < xlim) and (y >= 0) and (y < ylim):
                    c = x * 1000 + y
                    if c not in visited:
                        cords.append([x, y])
        for v in visited:
            ret.append([int(v / 1000), v % 1000])
        return ret
            
# medium: https://www.lintcode.com/problem/1892
