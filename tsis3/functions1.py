#--------FIRST--------#
def gramsToOunces(grams):
    return 28.3495231 * grams

print(gramsToOunces(5))

#--------SECOND--------#
def FarenheitToCentigrade(temp):
    return (temp - 32)*(5/9)

print(FarenheitToCentigrade(90))

#--------THIRD--------#
def solve(numheads, numlegs):
    numrabbits = numlegs/2 - numheads
    numchicken = numheads - numrabbits
    return int(numrabbits), int(numchicken)

print(solve(35, 94))

#--------FOURTH--------#
def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0: 
            return False
    return True

def filter_prime(numList):
    ansList = list()
    numListModified = numList.split()
    for num in numListModified:
        num_int = int(num)
        if is_prime(num_int):
            ansList.append(num_int)
    return ansList

print(filter_prime("1 2 5 43 23 4"))

#--------FIFTH--------#
def string_permutation(str, i = 0):
    if i == len(str):
        print("".join(str))
    for j in range(i, len(str)):
        words = [c for c in str]
        words[i], words[j] = words[j], words[i]
        string_permutation(words, i + 1)

str = input()
string_permutation(str)

#--------SIXTH--------#
def reverse_sentence(senten):
    sentenceList = senten.split()
    sentenceList.reverse()
    ansStr = ""
    for str in sentenceList:
        ansStr += str
        ansStr += " "
    return ansStr

print(reverse_sentence("We are ready"))

#--------SEVENTH--------#
def has_33(nums):
    n = len(nums)
    for i in range(0, n-2):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

#--------EIGHTH--------#
def spy_game(nums):
    n = len(nums)
    for i in range(0, n-3):
        if nums[i] == 0 and nums[i+1] == 0 and nums[i+2] == 7:
            return True
    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

#--------NINTH--------#
def sphere_volume(r):
    return (4/3)*3.14*(r**3)
    
print(sphere_volume(3))

#--------TENTH--------#
def uniq_list(list):
    ans_list = []
    for x in list:
        if x not in ans_list:
            ans_list.append(x)
    return ans_list

print(uniq_list([1,2,2,3, 5, 6, 5]))

#--------ELEVENTH--------#
def is_palindrome(str):
    if str == str[::-1]:
        return True
    return False

print(is_palindrome("madam"))
print(is_palindrome("madame"))

#--------TWELFTH--------#
def histogram(nums):
    for x in nums:
        str = ""
        for i in range(0, x):
            str += '*'
        print(str)

histogram([4, 9, 7])