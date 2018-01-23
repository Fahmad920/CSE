import random
words = random.choices(["creative", "art", "inspire", "dream", "color", "paint", "leaf", "heart", "wind", "follow"])
guesses_left = 10
correct_guess = False
letters_guessed = []
hidden_word = ["creative", "art", "inspire", "dream", "color", "paint", "leaf", "heart", "wind", "follow"]
listOne = list(words)
print(listOne)
guess_left = str(input("Guess a letter "))

# while guesses_left < 10:
# input(letters_guessed))
# print("You have guessed %s" % letter)
