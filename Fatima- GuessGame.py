import random
#print(random.randint(0, 50))


number = input("Guess a Number ")
if number == 25:
    print("Correct")
    if number != 25:
        print("Guess Again")


# def guess_right(number):
#     if number >= 25:
#         print("Correct")
#     elif number != 25:
#         print("Guess Again")


# github.com/MrWiebe/CSE7
# 1) get computer to generate a random number 1-50
# 2) get a number (input) from the user
# 3) compare number to input
# 4) Add "Higher" or "lower"
# 5) add 5 guesses
# for guesses, remove one
