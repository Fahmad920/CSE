import random

# Initializing Variables
answer = random.randint(1, 50)
turn = 5
correct_guess = False


# Describes exactly ONE turn. The while loop is the Game Controller.
while turn > 0 and correct_guess == False:
    guess = int(input("Guess a Number 1-50 "))
    if guess == answer:
        correct_guess = True
        print("You guessed right")
    elif guess < answer:
        print("Higher")
        turn -= 1
    elif guess > answer:
        print("Lower")
        turn -= 1

if turn == 0:
    print("Good Job, but that was not the answer. The correct answer was %s" % answer)

