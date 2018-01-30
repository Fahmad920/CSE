import random
import string


letters_guessed = []
hidden_words = ["creative", "art", "inspire", "dream", "color", "paint", "leaf", "heart", "wind", "follow"]
guesses_left = 10
words = random.choices(hidden_words)
newStr = ''.join(words)
listOne = list(newStr)
print(newStr)
letter = string. ascii_letters


while guesses_left > 0:
    for letter in newStr:
        if letter in letters_guessed:
            #else:
            # hide letters
            their_guess = input("Guess a letter ")
    if their_guess in newStr:
        print("You guessed it right!")
    else:
        guesses_left -= 1
        print("You are wrong!")
