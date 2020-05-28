class Solution:
    """
    @param target: the destination
    @return: the minimum number of steps
    """
    def reachNumber(self, target):
        # Write your code here
        '''
        思路解析：暴力法可以解，但是一定超时！
        1. target正负是等价的。
        2. 一直走，到大于等于target为止。如果相等，直接返回步数。
        3. 不相等，处理以下几种情况：(n一定比step小)
          1. 差n为偶数，找到之前的n步一负一正即可解决。步数不变。
          2. 差n为奇数，想办法把它变成偶数就和上面的情况一样了。
            1. 步数step为偶数，多走一步就是偶数了（n + (step + 1) = 偶数）。
            2. 步数step为奇数，必须多走两步（n + (step + 1) + (step + 2) = 偶数）
        '''
        target = int(math.fabs(target))
        pos, step = 0, 1
        while (pos < target):
            pos += step;
            step += 1
        step -= 1 # 总共走了几步
        if pos == target:
            return step
        pos -= target
        if (pos % 2) == 0:
            return step
        if (step % 2) == 0:
            return step + 1
        else:
            return step + 2

# easy: https://www.lintcode.com/problem/reach-a-number/
