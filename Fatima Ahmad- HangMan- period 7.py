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
    str1 = ''.join(output)
    print(str1)
    if "*" not in output:
        print("You Won")
        exit(0)

    their_guess = input("Guess a letter ")
    letters_guessed.append(their_guess)
    if their_guess in newStr:
        print("You guessed it right!")
        if guesses_left > 0 and their_guess in words:
            print("You have guessed the word, the word was %s" % words)
    else:
        guesses_left -= 1
        print("You are wrong!")

if guesses_left == 0:
    print("The correct word was %s" % newStr)


# if their_guess == output:
# guesses_left = 0
# print("You guessed the word. The word was %s" % newStr)
