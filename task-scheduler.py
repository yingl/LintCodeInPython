class Solution:
    """
    @param tasks: the given char array representing tasks CPU need to do
    @param n: the non-negative cooling interval
    @return: the least number of intervals the CPU will take to finish all the given tasks
    """
    def leastInterval(self, tasks, n):
        # write your code here
        # 1. 先按任务出现的次数排序
        # 2. 统计有多少个任务是小于最大出现次数的
        # 3. 计算因为n导致需要核外耗时的结果
        c = [0 for i in range(26)]
        for t in tasks:
             c[ord(t) - ord('A')] += 1
        c.sort()
        i = 25
        while (i >= 0) and (c[i] == c[-1]):
            i -= 1
        return max(len(tasks), (c[-1] - 1) * (n + 1) + 25 - i)

# medium: https://www.lintcode.com/problem/945
