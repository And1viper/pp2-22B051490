import math

#--------FIRST--------#
deg = int(input("Input degree: "))
print("Output radian: {}".format(math.radians(deg)))

#--------SECOND-------#
h = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))

area = h*((a+b)/2)
print("Expected Output: {}".format(area))

#--------THIRD-------#
num_sides = int(input("Input number of sides: "))
len_side = float(input("Input the length of a side: "))

# ang = math.pi/num_sides
# h = len_side/(2*math.tan(ang))
area = (num_sides*len_side*len_side)/(4*math.tan(math.pi/num_sides))
print("The area of the polygon is: {}".format(round(area, 4)))

#--------FOURTH-------#
a = float(input("Length of base: "))
h = float(input("Height of parallelogram: "))

print("Expected Output: {}".format((a*h)))


