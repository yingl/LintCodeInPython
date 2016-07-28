# -*- coding: utf-8 -*-

class Shape:
    def draw(self):
        raise NotImplementedError('This method should have implemented.')

class Triangle(Shape):
    # Write your code here
    def draw(self):
        print "  /\\"
        print " /  \\"
        print "/____\\"

class Rectangle(Shape):
    # Write your code here
    def draw(self):
        print " ----"
        print "|    |"
        print " ----"

class Square(Shape):
    # Write your code here
    def draw(self):
        print " ----"
        print "|    |"
        print "|    |"
        print " ----"

class ShapeFactory:
    # @param {string} shapeType a string
    # @return {Shape} Get object of type Shape
    def getShape(self, shapeType):
        # Write your code here
        if shapeType == 'Square':
            return Square()
        elif shapeType == 'Triangle':
            return Triangle()
        elif shapeType == 'Rectangle':
            return Rectangle()
        else:
            return None