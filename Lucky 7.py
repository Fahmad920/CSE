import random
seven = 7
money = 15
bet = 1
MaxRound = 0
HighMoney = 0
Round = 0
while money > 0:
    print("You have %s dollar" % money)
    D1 = int(random.randint(1, 6))
    D2 = int(random.randint(1, 6))
    print(D1 + D2)
    if D1 + D2 == seven:
        money += 4
    elif D1 + D2 != seven:
        money -= 1
    MaxRound += 1

if money == 0:
    print("You played %s rounds." % MaxRound)
    print("You lost all your money");

if HighMoney == MaxRound: