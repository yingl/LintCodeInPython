# coding: utf-8

class Toy:
    def talk(self):
        raise NotImplementedError('This method should have implemented.')

class Dog(Toy):
    # Write your code here
    def talk(self):
        print 'Wow'

class Cat(Toy):
    # Write your code here
    def talk(self):
        print 'Meow'

class ToyFactory:
    # @param {string} shapeType a string
    # @return {Toy} Get object of the type
    def getToy(self, type):
        # Write your code here
        if type == 'Dog':
            return Dog()
        elif type == 'Cat':
            return Cat()

# easy: http://lintcode.com/zh-cn/problem/toy-factory/
