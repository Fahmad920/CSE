import random
seven = 7
money = 15
bet = 1
MaxRound = 0
HighMoney = money
HighRound = 0
while money > 0:
    print("You have $%s" % money)
    D1 = int(random.randint(1, 6))
    D2 = int(random.randint(1, 6))
    print(D1 + D2)
    if D1 + D2 == seven:
        money += 4
        if money > HighMoney:
            HighMoney = money
            HighRound = MaxRound
    elif D1 + D2 != seven:
        money -= 1
    MaxRound += 1

print("You played %s rounds." % MaxRound)
print("You lost all your money")

print("Highest amount of money was $%s" % HighMoney)
print("You had the most money at round %s" % HighRound)
