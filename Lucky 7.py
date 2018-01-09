import random
D1 = int(random.randint(1, 6))
D2 = int(random.randint(1, 6))
print(D1 + D2)
seven = 7


money = 15
bet = 1
while money > 0:
    print("You have %s money" % money)

if D1 + D2 == seven:
    money += 5
