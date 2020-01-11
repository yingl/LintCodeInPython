class Solution:
    """
    @param pid: the process id
    @param ppid: the parent process id
    @param kill: a PID you want to kill
    @return: a list of PIDs of processes that will be killed in the end
    """
    def killProcess(self, pid, ppid, kill):
        # Write your code here
        ret = []
        di = {}
        for i in range(len(pid)):
            if ppid[i] not in di:
                di[ppid[i]] = [pid[i]]
            else:
                di[ppid[i]].append(pid[i])
        kills = [kill]
        while kills:
            ret.extend(kills)
            tmp = kills
            kills = []
            for k in tmp:
                if k in di:
                  kills.extend(di[k])
        return ret

# easy: https://www.lintcode.com/problem/kill-process/
