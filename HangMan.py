import random
import string


letters_guessed = []
hidden_words = ["creative", "art", "inspire", "dream", "color", "paint", "leaf", "heart", "wind", "follow"]
guesses_left = 10
words = random.choices(hidden_words)
newStr = ''.join(words)
listOne = list(newStr)
letter = string. ascii_letters


while guesses_left > 0:
    output = []
    for letter in newStr:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    print(output)

    their_guess = input("Guess a letter ")
    letters_guessed.append(their_guess)
    if their_guess in newStr:
        print("You guessed it right!")
    else:
        guesses_left -= 1
        print("You are wrong!")

if guesses_left == 0:
    print("The word was %s" % newStr)

if their_guess == newStr:
    guesses_left = 0
    print("You guessed the word. The word was %s" % newStr)
