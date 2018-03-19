class Item(object):
    def __init__(self, name):
        self.name = name

    def pick_up(self):
        print("%s picked up %s" % self.name)

    def drop(self):
        print("You dropped %s" % self.name)

    def trade(self):
        print("You traded %s" % self.name)


class Consumable(Item):
    def __init__(self, name):
        super(Consumable, self).__init__(name)

    def use(self):
        print("You use the %s" % self.name)

    def eat(self):
        print("You ate the %s" % self.name)


class Hay(Consumable):
    def __init__(self, name):
        super(Hay, self).__init__(name)

    def use(self):
        print("You give the hay to a horse.")


class Cake(Consumable):
    def __init__(self, name, color, taste):
        super(Cake, self).__init__(name)
        self.color = color
        self.taste = taste

    def use(self):
        print("This cake is used as a potion")

    def eat(self):
        print("You ate the cake, but now you will turn into a bear")


class Water(Consumable):
    def __init__(self, name, container):
        super(Water, self).__init__(name)
        self.container = container

    def drink(self):
        print("You drank %s" % self.name)


class Apple(Consumable):
    def __init__(self, name, color):
        super(Apple, self).__init__(name)
        self.color = color


class Weapon(Item):
    def __init__(self, name):
        super(Weapon, self).__init__(name)

    def fight(self):
        print("You attacked with %s" % self.name)


class Sword(Weapon):
    def __init__(self, name, sharpness):
        super(Sword, self).__init__(name)
        self.sharpness = sharpness

    def stab(self):
        print("You stabbed %s with the sword" % self.name)


class BowAndArrow(Weapon):
    def __init__(self, name):
        super(BowAndArrow, self).__init__(name)

    def shoot(self):
        print("You shot %s with the bow and arrow" % self.name)

    def carry(self):
        print("You picked up the %s" % self.name)


class Furniture(Item):
    def __init__(self, name):
        super(Furniture, self).__init__(name)

    def move(self):
        print("You moved the %s" % self.name)


class Tapestry(Furniture):
    def __init__(self, name):
        super(Tapestry, self).__init__(name)

    def mend(self):
        print("You mended the tapestry with %s." % self.name)


class Table(Furniture):
    def __init__(self, name, food):
        super(Table, self).__init__(name)
        self.food = food


class Rug(Furniture):
    def __init__(self, name, pattern):
        super(Rug, self).__init__(name)
        self.pattern = pattern


class BearStatue(Furniture):
    def __init__(self, name):
        super(BearStatue, self).__init__(name)

    def look_around(self):
        print("You looked around the %s" % self.name)


class Dresser(Furniture):
    def __init__(self, name, crown, mirror, necklace):
        super(Dresser, self).__init__(name)
        self.crown = crown
        self.mirror = mirror
        self.necklace = necklace


class Shield(Furniture):
    def __init__(self, name):
        super(Shield, self).__init__(name)

    def protect(self):
        print("You used the %s as protection" % self.name)


class WoodCarving(Furniture):
    def __init__(self, name, bear):
        super(WoodCarving, self).__init__(name)
        self.bear = bear

    def buy(self):
        print("You bought %s" % self.name)


class Magic(Item):
    def __init__(self, name):
        super(Magic, self).__init__(name)

    def make(self):
        print("You made a %s with a potion" % self.name)


class Potion(Magic):
    def __init__(self, name, cake):
        super(Potion, self).__init__(name)
        self.cake = cake

    def transform(self):
        print("You consumed the potion and now you transformed into a %s" % self.name)


class WillowtheWisp(Magic):
    def __init__(self, name):
        super(WillowtheWisp, self).__init__(name)

    def follow(self):
        print("You followed the Willow the Wisp" % self.name)

    def appear(self):
        print("The %s appeared in front of you" % self.name)


class Misc(Item):
    def __init__(self, name):
        super(Misc, self).__init__(name)


class NeedleAndThread(Misc):
    def __init__(self, name):
        super(NeedleAndThread, self).__init__(name)

    def sew(self):
        print("You sewed the %s with the needle and thread " % self.name)


class Container(Misc):
    def __init__(self, name, items):
        super(Container, self).__init__(name)
        self.inventory = items

    def open(self):
        print("You opened the %s" % self.name)

    def put_in(self):
        print("You put %s into the %s" % (self.name, self.name))

    def take_out(self):
        print("You took %s out of the %s" % (self.name, self.name))

    def carry(self):
        print("You are carrying the %s" % self.name)

    def close(self):
        print("You closed the %s" % self.name)


class SpecialNecklace(Misc):
    def __init__(self, name):
        super(SpecialNecklace, self).__init__(name)

    def wear(self):
        print("You are wearing the %s" % self.name)

    def place(self):
        print("You placed the necklace in the %s" % self.name)
