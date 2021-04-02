class Solution:
    """
    @param employees: information of the employees
    @param friendships: the friendships of employees
    @return: return the statistics
    """
    def departmentStatistics(self, employees, friendships):
        # write your code here.
        result = {}
        bud = {}
        for line in employees:
          _id, _, bu = line.split(', ')
          bud[_id] = bu
          if bu not in result:
            result[bu] = [set([]), 0]
          result[bu][1] += 1
        for f in friendships:
          id1, id2 = f.split(', ')
          if bud[id1] != bud[id2]:
            result[bud[id1]][0].add(id1)
            result[bud[id2]][0].add(id2)
        ret = []
        for k, v in result.items():
          r = k + ': '
          r += str(len(v[0])) + ' of ' + str(v[1])
          ret.append(r)
        return ret

# easy: https://www.lintcode.com/problem/department-statistics/
