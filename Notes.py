# print("Hello World")
#
# #Keep loving who you are- Harris J (use ctrl / to toggle comment)
#
# print(3 + 5)
# print(5 - 3)
# print(5 * 3)
# print(6 / 2)
# print(3 ** 2)
#
# print("see if you can figure this out")
# print(5 % 3)
#
# # variables
# car_name = "Weibe Mobile"
# car_type = "lamborghini Seto Elemento"
# car_cylinders = 8
# car_mpg = 9000.1
#
# # Inline Printing
# print("My car is the %s. It is a %s" % (car_name, car_type))
#
# # Taking input
# name = input("What is your name?")
# print("Hello %s." % name)
# # print(name)
#
# age = input("What is your age? ")
# print("Your old %s." % age)
# print("You are still a teenager")
#
#
#
#
#
# # Change to the file
# def print_hw() :
#     print("Hello World")
#
#
# print_hw()
#
#
# def say_hi(name):    # name is a "parameter"
#     print("Hello %s" % name)
#     print("I hope you have a fantastic day.")
#
#
# say_hi("Harris J")
#
#
# def birthday(age):
#     age += 1 # age = age + 1
#     print(age)
#
#
# say_hi("Harris J")
# print("Harris J is 20. Next year:")
# birthday(20)
# press ctrl-A and ctrl -/
# to comment everything out


#def f(x):
  #  return x**5 + 4 * x ** 4 - 17*x**2 +4


#print(f(3))
#print(f(3) + f(5))


# If statements


def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:  # Else If
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else :
        return "F"

# Loops


# for num in range(5):
#     print(num + 1)

# for mystery in "Hello World":
#     print(mystery)

# a = 1
# while a < 10:
#     print(a)
#     a += 1
#
# response = ""
# while response != "Hello":
#     response = input("Say \\ \"Hello\"")
#
# print("Hello \nWorld")    # \n means newline

import random #imports should be at the top
print(random.randint(0, 6))












































