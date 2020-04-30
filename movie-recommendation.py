import functools

class Solution:
    def minMalwareSpread(self, graph):
        movies_viewed_by = {} # 电影被哪些人看过
        for i in range(len(graph)):
            for m in graph[i]:
                if m not in movies_viewed_by:
                    movies_viewed_by[m] = set([])
                movies_viewed_by[m].add(i)
        ret = []
        candidates = {}
        for u in range(len(graph)):
            candidates[u] = {}
            for m in graph[u]:
                for _u in movies_viewed_by[m]:
                    if _u != u:
                        for _m in graph[_u]:
                            if _m not in graph[u]:
                                if _m not in candidates[u]:
                                    candidates[u][_m] = 0
                                candidates[u][_m] += 1
            def cmp(x, y): # 排序规则坑爹
                if x[1] < y[1]:
                    return 1
                elif x[1] == y[1]:
                    if x[0] < y[0]:
                        return -1
                    elif x[0] == y[0]:
                        return 0
                    else:
                        return 1
                else:
                    return -1
            arr = sorted(candidates[u].items(), key=functools.cmp_to_key(cmp))
            ret.append([])
            for i in range(len(arr)):
                if (i < 5):
                    ret[-1].append(arr[i][0])
                else:
                    break
            if u == 9:
                print(ret[-1])
        return ret
        
# easy: https://www.lintcode.com/problem/movie-recommendation/description
