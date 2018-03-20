class Character(object):
    def __init__(self, name, description, item, health, location, tree, damage=10):
        self.name = name
        self.description = description
        self.inventory = []
        self.item = item
        self.health = health
        self.damage = damage
        self.alive = False
        self.location = location
        self.tree = tree

    def look(self):
        print(self.location.name)
        print("You have looked around")

    def climb(self):
        print(self.tree.location)
        print("You have looked around")

    def take(self, item):
        self.inventory.append(item)
        print("You have taken something")

    def health(self):
        print(self.name.damage)
        print("You have health")

    def take_damage(self, amt):
        if self.health <= 0:
            print("%s is already dead" % self.name)
            return
        self.health -= amt
        if self.health <= 0:
            self.alive = False
            print("%s has died." % self.name)

    def attack(self, target):
        if self.alive:
            print("%s attacks %s. %s's health is %d. The enemy's health is %d." % (self.name, target.name, self.name,
                                                                                   self.health,
                                                                                   target.health))
            target.take_damage(self.damage)
        else:
            print("%s is dead and cannot attack" % self.name)


player = Character("name", "description", None, 100, None, 10)
enemy = Character("Enemy", "It's an enemy", 100, None, None, 10)

player.attack(enemy)
player.attack(enemy)
player.attack(enemy)
player.attack(enemy)
player.attack(enemy)
player.attack(enemy)

enemy.attack(player)
print("%s's health is %s." % (player.name, player.health))
print("%s's health is %s." % (enemy.name, enemy.health))


class Merida(Character):
    def __init__(self, name, description, item, health, location, tree, bow_and_arrow, special_necklace):
        super(Merida, self).__init__(name, description, item, health, location, tree,)
        self.bow_and_arrow = bow_and_arrow
        self.special_necklace = special_necklace

    def walk(self):
        print("% has moved" % self.name)


class Queen(Character):
    def __init__(self, name, description, item, health, location, tree, crown):
        super(Queen, self).__init__(name, description, item, health, location, tree)
        self.crown = crown

    def transform(self):
        print("After the Queen ate the %s Merida gave her, the Queen transformed into a bear." % self.name)
