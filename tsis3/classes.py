#--------FIRST--------#
class StringOperator:
    def getString(self):
        self.str = input()
    def printString(self):
        print(self.str.upper())

# str = StringOperator()
# str.getString()
# str.printString()

#--------SECOND--------#
class Shape:
    def area(shapeArea = 0):
        print(shapeArea)

class Square(Shape):
    def __init__(self, length):
        self.length = length
        self.squareArea = length*length
    def squareArea(self):
        super().area(self.area)

square = Square(int(input))
square.squareArea()

#--------THIRD--------#

#--------FOURTH--------#

#--------FIFTH--------#

#--------SIXTH--------#