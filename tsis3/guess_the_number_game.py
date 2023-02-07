import random

name = input("Hello! What is your name?\n")

print("Well,", name, ", I am thinking of a number between 1 and 20.")

wrong_ans = True
random_num = random.randint(1,20)
guess_num = 0
while wrong_ans:
    guess = int(input("Take a guess.\n"))
    guess_num+=1
    if guess > random_num:
        print("Your guess is too high.")
    elif guess < random_num:
        print("Your guess is too low.")
    else:
        wrong_ans = False
print("Good job,", name, "! You guessed my number in", guess_num, "guesses!")