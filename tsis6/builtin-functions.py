import math
import time
#--------FIRST--------#
list = [1, 2, 3, 5]
ans = math.prod(list)
print(ans)

#--------SECOND--------#
string = "asdsasAdsddSDS"
lower_cnt = 0
upper_cnt = 0
for c in string:
    if c.islower():
        lower_cnt += 1
    elif c.isupper():
        upper_cnt += 1
print("# of lower:", lower_cnt, "\n# of upper:", upper_cnt)

#--------THIRD--------#
palin = "clueeulc"
not_palin = "palindrome"
print("{}: {} and {}: {}".format(palin, palin == ''.join(reversed(palin)), not_palin, not_palin == ''.join(reversed(not_palin))))

#--------FOURTH--------#
num = int(input())
mil_s = int(input())
time.sleep(mil_s/1000)
sqrt = num ** (0.5)
print(f'Square root of {num} after {mil_s} miliseconds is {sqrt}')

#--------FIFTH--------#
true_tuple = (True, True, True)
false_tuple = (True, False)
numeric_tuple = (1, 2, 3)
print(all(true_tuple), all(false_tuple), all(numeric_tuple))
