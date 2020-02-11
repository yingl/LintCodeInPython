class Solution:
    """
    @param commands: type: List[int]
    @param obstacles: type: List[List[int]]
    @return: Return the square of the maximum Euclidean distance
    """
    def robotSim(self, commands, obstacles):
        # write your code here
        pos = [0, 0]
        dirs = ((0, 1), (-1, 0), (0, -1), (1, 0)) # 初始方向向上，逆时针方向转。
        dir_idx = 0 # 初始方向向上
        for c in commands:
            if c == -1: # 右转90度，数组向左循环移动。
                dir_idx = abs(dir_idx - 1 + 4) % 4
            elif c == -2: # 左转90度，数组向右循环移动。
                dir_idx = (dir_idx + 1) % 4
            _dir = dirs[dir_idx]
            if (c >= 1) and (c <= 9):
                while c > 0:
                    c -= 1
                    next_pos = [pos[0] + _dir[0], pos[1] + _dir[1]] # 下一步位置
                    if next_pos in obstacles:
                        break
                    else:
                        pos = next_pos # 更新位置
        return pos[0] * pos[0] + pos[1] * pos[1]

# easy: https://www.lintcode.com/problem/walking-robot-simulation/
