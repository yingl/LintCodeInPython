# coding: utf-8

class Solution:
    """
    @param source: A string
    @param target: A string
    @return: A string denote the minimum window
             Return "" if there is no such a string
    """
    def minWindow(self, source, target):
        # write your code here
        s_status = [0] * 256  # 如果匹配，那么s对应字符出现的次数不应小于target对应字符出现的次数。
        t_status = [0] * 256  # 
        for ch in target:
            t_status[ord(ch)] += 1
        window = 2147483647
        matched = 0
        start = 0
        j = 0
        for i in xrange(len(source)):
            if matched < len(target):
                if s_status[ord(source[i])] < t_status[ord(source[i])]:
                    matched += 1
                s_status[ord(source[i])] += 1
            if matched == len(target):
                # 从头看删除哪些字符后依然可以保证匹配
                while j <= i:
                    if s_status[ord(source[j])] > t_status[ord(source[j])]:
                        s_status[ord(source[j])] -= 1
                        j += 1
                    else:
                        break
                # 调整窗口大小
                if window > (i - j + 1):
                    window = i - j + 1
                    start = j # substr的开始位置
                # 继续调整，直到matched不满足
                while (j <= i) and (matched == len(target)):
                    s_status[ord(source[j])] -= 1
                    if s_status[ord(source[j])] < t_status[ord(source[j])]:
                        matched -= 1  # 意味着必需在后面再次匹配source[j]
                    j += 1  # 必需确保这里加1，删除的元素跳过。
        return source[start:start + window] if (window != 2147483647) else ''

# medium: http://lintcode.com/zh-cn/problem/minimum-window-substring/
