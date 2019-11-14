# coding: utf-8

class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        # write your code here
        '''
        其实题目里隐含了一个很重要的推论：
        如果在a[i]停车加满油仍然开不到a[j]的话，
        那么即使在a[i]不停，在a[i + k]加满油也到不了a[j]。
        因为即使a[i]停了，a[i ＋ k]还是可以停的。
        '''
        i = 0
        number = len(gas)
        while i < number:
            j = i # 从i出发
            count = 1
            gas_count = 0 # 初始汽油量
            while count <= number:
                if (gas_count + gas[j % number] >= cost[j % number]): # 在第j个站加油后可以开到下个站
                    if count == len(gas): # 正好环游一圈
                        return i
                    gas_count += gas[j % number] - cost[j % number] # 到下一站时剩下的油量
                    j += 1  # 去下一站
                    count += 1
                else:
                    i = j + 1 # 既然从i点不行，利用上面的推论，我们从j + 1开始尝试。
                    break
        return -1

# medium: http://lintcode.com/zh-cn/problem/gas-station/
