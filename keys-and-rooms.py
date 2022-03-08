from typing import (
    List,
)

class Solution:
    """
    @param rooms: a list of keys rooms[i]
    @return: can you enter every room
    """
    def can_visit_all_rooms(self, rooms: List[List[int]]) -> bool:
        # Write your code here
        ret = 1
        visited = [0] * len(rooms)
        visited[0] = 1
        keys = [rooms[0], []]
        curr = 0
        while keys[curr]:
            for k in keys[curr]:
                if visited[k] == 0:
                    for _k in rooms[k]:
                        if visited[_k] == 0:
                            keys[1 - curr].append(_k)
                    visited[k] = 1
                    ret += 1
            keys[curr].clear()
            curr = 1 - curr
        return ret == len(rooms)
      
# medium: https://www.lintcode.com/problem/1428
