class Item(object):
    def __init__(self, name):
        self.name = name

    def pick_up(self):
        print("You picked up %s" % self.name)

    def drop(self):
        print("You dropped %s" % self.name)


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


class Weapon(Item):
    def __init__(self, name):
        super(Weapon, self).__init__(name)

    def fight(self):
        print("You attacked with %s" % self.name)


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


class Magic(Item):
    def __init__(self, name):
        super(Magic, self).__init__(name)

    def make(self):
        print("You made a %s with a potion" % self.name)


class Misc(Item):
    def __init__(self, name):
        super(Misc, self).__init__(name)


class NeedleAndThread(Misc):
    def __init__(self, name):
        super(NeedleAndThread, self).__init__(name)

    def sew(self):
        print("You sewed the %s with the needle and thread " % self.name)


class Sack(Misc):
    def __init__(self, name):
        super(Sack, self).__init__(name)

    def open(self):
        print("You opened the %s" % self.name)

    def put_in(self):
        print("You put %s into the sack" % self.name)

    def take_out(self):
        print("You took %s out of the sack" % self.name)

    def carry(self):
        print("You are carrying the sack with %s" % self.name)

    def close(self):
        print("You closed the sack with %s in it" % self.name)


class Crate(Misc):
    def __init__(self, name):
        super(Crate, self).__init__(name)

    def open(self):
        print("You opened the crate")

    def close(self):
        print("You closed the crate")

    def remove(self):
        print("You removed %s from the crate" % self.name)

    def place(self):
        print("You placed %s back into the crate" % self.name)

    def replace(self):
        print("You replaced %s with %s" % self.name)

    def move(self):
        print("You moved the crate somewhere else" % self.name)


class Necklace(Misc):
    def __init__(self, name):
        super(Necklace, self).__init__(name)

    def trade(self):
        print("You traded the necklace for %s" % self.name)

    def wear(self):
        print("You are wearing the necklace")

    def place(self):
        print("You placed the necklace in the %s" % self.name)
