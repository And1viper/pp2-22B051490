#--------FIRST--------#
N = 10

def square_gen(num):
    cur = 1
    while cur < num + 1:
        yield cur*cur
        cur += 1

squareOut = square_gen(N)
print("First exersice: ")
for i in squareOut:
    print(i)

#--------SECOND--------#
n = int(input("Enter number for 2nd exersice: "))

def even_gen(num):
    cur = 0
    while cur < num + 1:
        yield cur
        cur += 2

print(", ".join(map(str, even_gen(n))))

#--------THIRD--------#
n = 30

def div_gen(num):
    cur = 0
    while cur < num+1:
        if cur%12 == 0:
            yield cur
        cur+=1

# print(", ".join(map(str, div_gen(n))))

#--------FOURTH--------#
a = 5
b = 12

def squares(a, b):
    cur = a
    while cur < b+1:
        yield cur*cur
        cur+=1

for i in squares(a, b):
    print(i)

#--------FIFTH--------#
n = 10

def reverse_gen(num):
    cur = num
    while cur > -1:
        yield cur
        cur -= 1

# for i in reverse_gen(n):
#     print(i)