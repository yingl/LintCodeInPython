class Solution:
    """
    @param color: the given color
    @return: a 7 character color that is most similar to the given color
    """
    def similarRGB(self, color):
        # Write your code here
        # RGB三个颜色分开找，可以用二分法优化，这里偷懒暴力了。
        ret = '#'
        for i in (1, 3, 5):
            c = self.find_nearest_color(color[i:i+2])
            ret += c
        return ret
        
    def find_nearest_color(self, color):
        ret = ''
        diff = 256
        color = int(color, 16)
        colors = [0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff]
        for _color in colors:
            if abs(_color - color) < diff:
                diff = abs(_color - color)
            ret = _color
        return self.to_hex(ret)
        
    def to_hex(self, i):
        return hex(i)[2:]

# easy: https://www.lintcode.com/problem/similar-rgb-color/description
