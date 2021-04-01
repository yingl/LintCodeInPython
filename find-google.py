class Solution:
    """
    @param S: The c++ file
    @return: return if there is "Google" in commet line
    """
    def FindGoogle(self, S):
        # Write your code here.
        lc = False # // 形式的注释
        mlc = False # /* ... */ 形式的注释
        google = ''
        for s in S:
          prev = None
          for c in s:
            if (prev == '/') and (c == '/') and (not mlc):
              lc = True
            elif (prev == '/') and (c == '*') and (not mlc) and (not lc):
              mlc = True
            elif (prev == '*') and (c == '/') and mlc:
              mlc = False
            elif lc or mlc:
              if c == 'G':
                google = 'G'
              elif (c == 'o') and (google == 'G'):
                google = 'Go'
              elif (c == 'o') and (google == 'Go'):
                google = 'Goo'
              elif (c == 'g') and (google == 'Goo'):
                google = 'Goog'
              elif (c == 'l') and (google == 'Goog'):
                google = 'Googl'
              elif (c == 'e') and (google == 'Googl'):
                return True
              else:
                google = ''
            prev = c
          lc = False
        return False
      
# easy: https://www.lintcode.com/problem/find-google/
