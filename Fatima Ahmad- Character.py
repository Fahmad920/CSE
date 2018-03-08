import random


class Character(object):
    def __init__(self, name, description, item, health, damage=10):
        self.name = name
        self.description = description
        self.inventory = []
        self.item = item
        self.health = health
        self.damage = damage


    def look(self):
        print("You have looked around")

    def climb(self):
        print("You have looked around")

    def take(self, item):
        self.inventory.append(item)
        print("You have taken something")

    def health(self):
        print("You have health")

    def take_damage(self, amt):
        self.health -= amt

    def attack(self, target):
        if self.alive:
            target.take_damage(self.damage)
        else:
            print("%s is dead and cannot attack" % self.name)

player = Character("You", "Description", 100, None, None, 20)
enemy = Character("Enemy", "It's an enemy", 100, None, None)

player.attack(enemy)
enemy.attack(player)
print(player.health)
print(enemy.health)
