import random
# print(random.randint(0, 50))


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
