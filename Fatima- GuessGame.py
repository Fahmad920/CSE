import random
answer = (random.randint(1, 50))
print(answer)
guess = int(input("Guess a Number "))
turn = 5


def guess_number(number):
    if int("number") == int("answer)"):
        print("You Guessed Correctly")
        if int("number") <= int("answer"):
            print("Guess Lower")
            if int("number") >= int("answer"):
                print("Guess Higher")


turn = -1