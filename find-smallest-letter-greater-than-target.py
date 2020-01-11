class Solution:
    """
    @param letters: a list of sorted characters
    @param target: a target letter
    @return: the smallest element in the list that is larger than the given target
    """
    def nextGreatestLetter(self, letters, target):
        # Write your code here
        ret = None
        # diff = 100
        s = set(letters)
        while True:
            if target == 'z':
                target = 'a'
            else:
                target = chr(ord(target) + 1)
            if target in s:
                return target

# easy: https://www.lintcode.com/problem/find-smallest-letter-greater-than-target/
