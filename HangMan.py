import random
words = random.choices(["creative", "art", "inspire", "dream", "color", "paint", "leaf", "heart", "wind", "follow"])
guesses_left = 10
correct_guess = False
letters_guessed = []
hidden_word = ["creative", "art", "inspire", "dream", "color", "paint", "leaf", "heart", "wind", "follow"]
str1 = letters_guessed
listOne = list(str1)
print(words)

current_guess = ""
while current_guess != 'quit':
    current_guess = input("Guess a letter ")
    if current_guess == letters_guessed:
        newStr = "".join(letters_guessed)
str1 = letters_guessed
print(letters_guessed)

