# coding: utf-8

class Solution:
    # @param airplanes, a list of Interval
    # @return an integer
    def countOfAirplanes(self, airplanes):
        # write your code here
        '''
        以数据[[1, 10], [2, 3], [5, 8], [4, 7]]为例
        1. 字典air_status记录某时刻飞机增加或减少1架，1增加，-1减少。
          - a[1], a[2], a[5], a[4] = 1
          - a[10], a[3], a[8], a[7] = -1
        2. 把全部时刻放在一起排序:［1, 2, 3, 4, 5, 7, 8, 10]
        3. 遍历步骤2的结果，根据字典加减飞机数目
        '''
        ret = 0
        air_status = {}
        for air in airplanes:
            if air.start not in air_status:
                air_status[air.start] = 1
            else:
                air_status[air.start] += 1
            if air.end not in air_status:
                air_status[air.end] = -1
            else:
                air_status[air.end] -= 1
        time_order = []
        for key in air_status:  # Python不像C++有set
            time_order.append(key)
        time_order.sort()
        airs = 0
        for t in time_order:
            airs += air_status[t]
            ret = max(airs, ret)
        return ret

# medium: http://lintcode.com/zh-cn/problem/number-of-airplanes-in-the-sky/
