# # # print("Hello World")
# # #
# # # # Keep loving who you are- Harris J (use ctrl / to toggle comment)
# # #
# # # print(3 + 5)
# # # print(5 - 3)
# # # print(5 * 3)
# # # print(6 / 2)
# # # print(3 ** 2)
# # #
# # # print("see if you can figure this out")
# # # print(5 % 3)
# # #
# # # # variables
# # # car_name = "Weibe Mobile"
# # # car_type = "lamborghini Seto Elemento"
# # # car_cylinders = 8
# # # car_mpg = 9000.1
# # #
# # # # Inline Printing
# # # print("My car is the %s. It is a %s" % (car_name, car_type))
# # #
# # # # Taking input
# # # name = input("What is your name?")
# # # print("Hello %s." % name)
# # # print(name)
# # #
# # # age = input("What is your age? ")
# # # print("Your old %s." % age)
# # # print("You are still a teenager")
# # #
# # #
# # # # Change to the file
# # # def print_hw():
# # #     print("Hello World")
# # #
# # #
# # # print_hw()
# # #
# # # name is a "parameter"
# #
# #
# # def say_hi(name1):
# #     print("Hello %s" % name1)
# #     print("I hope you have a fantastic day.")
# #
# # say_hi("Harris J")
# #
# #
# #
# # #
# # #
# # # def birthday(age1):
# # #     age1 += 1  # age = age + 1
# # #     print(age1)
# # #
# # #
# # # say_hi("Harris J")
# # # print("Harris J is 20. Next year:")
# # # birthday(20)
# # # # press ctrl-A and ctrl -/
# # # # to comment everything out
# # #
# # #
# # # def f(x):
# # #     return x**5 + 4 * x ** 4 - 17*x**2 + 4
# # #
# # #
# # # print(f(3))
# # # print(f(3) + f(5))
# # #
# # #
# # # # If statements
# # #
# # #
# # # def grade_calc(percentage):
# # #     if percentage >= 90:
# # #         return "A"
# # #     elif percentage >= 80:   Else If
# # #         return "B"
# # #     elif percentage >= 70:
# # #         return "C"
# # #     elif percentage >= 60:
# # #         return "D"
# # #     else:
# # #         return "F"
# # #
# # # # Loops
# # #
# # # for num in range(5):
# # #     print(num + 1)
# # #
# # # for mystery in "Hello World":
# # #     print(mystery)
# # #
# # # a = 1
# # # while a < 10:
# # #     print(a)
# # #     a += 1
# # # #
# # # # response = ""
# # # # while response != "Hello":
# # # #     response = input("Say \\ \"Hello\"")
# # # #
# # # # print("Hello \nWorld")    # \n means newline
# #
# # #imports should be at the top
# #
# # # import random
# # # print(random.randint(0, 6))
# ## str (40) == "40" is true statement
#
# # comparisons
# print(1 == 1)   # Two equal signs to compare
# print(1 != 2)   # One is not equal to 2
# print(not False)  # This prints "True"
# print(1 == 1 and 5 <= 5)   # "and" statements check to see if both statements are true
# print(1 < 0 or 5 > 1)
#
#
# # Recasting
# c = "1"
# print(c == 1) # False - C is a string, but 1 is an integer
# print(int(c) == 1) # Compares two ints
# print(c == str(1)) # compares two strings
#
#
# # 1) get computer to generate a random number 1-50
# # 2) get a number (input) from the user
# # 3) compare number to input
# # 4) Add "Higher" or "lower"
# # 5) add 5 guesses
# # for guesses, remove one
# # github.com/MrWiebe/CSE7
#


# BlackJack Guide Line
# get two cards or number
# add up the cards to see the total value of two cards
# if cards are less than 17 then hit
# if the card are over 21 then bust
# if cards are close to 17 then stay


# lists

the_count = [1, 2, 3, 4, 5]
characters = ["graves", "Dory", "Boots", "Dora", "Shrek", "Obi-wan", "Carl"]
print(characters[0])
print(characters[3])

print(len(characters))  # Gives you the length of the list

# Going through lists
for char in characters:
    print(char)

for num in the_count:
    print(num ** 2)

len(characters)
range(3)   # makes a list of the numbers from 0 to 2
range(len(characters))  # Makes a list of ALL INDICES


for num in range(len(characters)):
    char = characters[num]
    print("The character at index %d is %s" % (num, char))

str1 = "Hello World!"
listOne = list(str1)
print(listOne)
listOne[11] = '.'
print(listOne)
newStr = "".join(listOne)
print(newStr)
print(listOne[-2])

# adding stuff to a list
characters.append("Belle")
print(characters)

# removing things from a list
characters.remove("Carl")
print(characters)

characters.pop(6)
print(characters)


# the string class
# import string
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.digits)
# print(string.punctuation)

# make sure to automatically make the punctuation to show up
# make comparison with upper case and lower case letters

strTwo = 'ThIs sEntENcE iS uNuSuAl'
lowercase = strTwo.lower()
print(lowercase)


# ""
# Outline of Hangman
# 1. Make a word bank - 10 items
# 2. Select a random item from the list
# 3. Add user input to a list of letters_guessed
# 4. Build a list of letters to show, and display the string form
# 5. Create the win condition

# keep track of turns
# guess_left = 10  loose a turn when the letter is wrong
# letters_gueesed = ['e', 'c', 'd', 'r']
# listform['A', '_', '_', '_']

# while guess > 0 and correct_guess == False:
# if guess == words:
# correct_guess == True
# print("You guessed the letter right")
# elif guess == False:
# print("That's not a letter. Guess again")

# Dictionaries - make up a key: value pair
dictionary = {'name': 'Lance', 'age': 18, "height": 6 * 12 + 2}

# Accessing from a dictionary
print(dictionary['name'])
print(dictionary['age'])
print(dictionary['height'])


# Adding to a dictionary
dictionary["eye color"] = "blue"
dictionary["paper towls"] = True
print(dictionary)

large_dictionary = {
    "California": "CA",
    "Michigan": "MI",
    "Florida": "FL"
}
print(large_dictionary['Florida'])

larger_dictionary = {
    "California": [
        "Sacremento",
        "Los Angles",
        "Fresno"
    ],
    "Washington": [
        "Seattle",
        "Tacoma",
        "Olympia",
        "Spokane",
    ],
    "Illinois": [
        "Chicago",
        "Naperville",
        "Peoria",
    ]
}

print(larger_dictionary["Illinois"])
print(larger_dictionary["Illinois"][0])

print(larger_dictionary["Washington"][3])


largest_dictionary = {
    "CA": {
        'NAME': "California",
        'POPULATION': 39250000,
        'BORDER ST': [
            'Oregon',
            'Nevada',
            'Arizona'
        ]
    },
    "MI": {
        "NAME": "Michigan",
        "POPULATION": 9928000,
        "BORDER ST": [
            'Wisconsin',
            'Ohio',
            'Indiana'
        ]
    },
    "FL": {
        "NAME": "Florida",
        "POPULATION": 20610000,
        "BORDER ST": [
            'Georgia',
            'Alabama',

        ]
        }
    }

print(largest_dictionary["FL"]["NAME"])
print(largest_dictionary["MI"]["NAME"])

