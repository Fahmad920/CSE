import random
import string
hidden_words = ["creative", "art", "inspire", "dream", "color", "paint", "leaf", "heart", "wind", "follow"]
guesses_left = 10
words = random.randint(0, 9)
correct_guess = hidden_words[words]
print(correct_guess)
letters_guessed = []
list1 = hidden_words

letters = string.ascii_lowercase


# words = ascii.lowercase

# for letter in words:
# if letter == words:
# set(words(ascii.lowercase))
# elif(letter != words)


current_guess = ""
while current_guess != 'quit':
    current_guess = input("Guess a letter ")
    if current_guess == letters_guessed:
        newStr = "".join(letters_guessed)
str1 = letters_guessed
print(letters_guessed)

