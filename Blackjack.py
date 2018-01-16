import random

turn = 0
card1 = random.randint(1, 10)
card2 = random.randint(1, 10)
print(card1 + card2)
print("Your cards are %s" % card1, card2)
print (int(input("Do you want to hit or stay "))

if "hit":
    turn += 1
elif "stay":
    turn = 0
