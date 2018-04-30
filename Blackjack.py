import random


def draw_hit():
    return random.randint(1, 10)


def total_value():
    return


card1 = draw_hit()
card2 = draw_hit()
print(card1 + card2)
print("Your cards are %s" % card1, card2)
turn = input("Do you want to hit or stay? ")

if "hit":
    print("You got %s." % draw_hit())
    print("Your total is now %s" % (value))
