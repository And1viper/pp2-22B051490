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
    def shapeArea(self, shapeArea = 0):
        print(shapeArea)

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def squareArea(self):
        super().shapeArea(self.length*self.length)

# square = Square(int(input()))
# square.squareArea()

#--------THIRD--------#
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def rectangleArea(self):
        super().shapeArea(self.length*self.width)

# rectangle = Rectangle(int(input()), int(input()))
# rectangle.rectangleArea()

#--------FOURTH--------#
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)
    def move(self, newX, newY):
        self.x = newX
        self.y = newY
    def dist(self, another):
        print(((self.x - another.x)**2 + (self.y - another.y)**2)**0.5)

# p1 = Point(1, 2)
# p2 = Point(5, 4)

# p1.show()
# p1.move(4, 5)
# p1.show()

# p1.dist(p2)

#--------FIFTH--------#
class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Success!\nYour balance: {}".format(self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal is impossble: the amount is more than your balance.\nYour balance: {}".format(self.balance))
        else:
            self.balance -= amount
            print("Success!\nYour balance: {}".format(self.balance))

owner = Account("Freeman", 12000)

owner.deposit(5000)

owner.withdraw(20000)

owner.withdraw(15000)

#--------SIXTH--------#
def prime_filter(numList):
    return filter(lambda x: all(x % i != 0 for i in range(2, x)), numList)
print(list(prime_filter([1, 2, 3, 6, 8, 10, 11])))