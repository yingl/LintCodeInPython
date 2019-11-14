# coding: utf-8

class Rectangle:

    '''
     * Define a constructor which expects two parameters width and height here.
    '''
    # write your code here
    
    '''
     * Define a public method `getArea` which can calculate the area of the
     * rectangle and return.
    '''
    # write your code here
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def getArea(self):
        return self.width * self.height

# naive: http://lintcode.com/zh-cn/problem/rectangle-area/
