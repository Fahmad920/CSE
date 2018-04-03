# Any import statements
class Item(object):
    def __init__(self, name):
        self.name = name

    def pick_up(self, person):
        print("%s picked up %s" % person.name, self.name)

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
    def __init__(self, name, container, person):
        super(Water, self).__init__(name)
        self.container = container
        self.person = person

    def drink(self, person):
        print("%s drank water" % person.name, self.name)


class Apple(Consumable):
    def __init__(self, name, color):
        super(Apple, self).__init__(name)
        self.color = color


class Weapon(Item):
    def __init__(self, name):
        super(Weapon, self).__init__(name)

    def fight(self, person):
        print("%s attacked with %s" % person.name, self.name)


class Sword(Weapon):
    def __init__(self, name, sharpness):
        super(Sword, self).__init__(name)
        self.sharpness = sharpness

    def stab(self, person):
        print("You stabbed %s with the sword" % person.name)


class BowAndArrow(Weapon):
    def __init__(self, name):
        super(BowAndArrow, self).__init__(name)

    def shoot(self, person):
        print("You shot %s with the bow and arrow" % person.name)

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

    def buy(self, person):
        print("You bought %s from %s" % self.name, person.name)


class Magic(Item):
    def __init__(self, name):
        super(Magic, self).__init__(name)

    def make(self):
        print("You made %s with magic" % self.name)


class Potion(Magic):
    def __init__(self, name, cake):
        super(Potion, self).__init__(name)
        self.cake = cake

    def transform(self, person):
        print("%s consumed the %s and now you transformed into a bear" % person.name, self.name)


class WillowtheWisp(Magic):
    def __init__(self, name):
        super(WillowtheWisp, self).__init__(name)

    def follow(self, person):
        print("%s followed the Willow the Wisp" % person.name, self.name)

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

    def open(self, person):
        print("You opened the %s" % person.name, self.name)

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

    def wear(self, person):
        print("%s are wearing the %s" % person.name, self.name)

    def place(self):
        print("You placed the necklace in the %s" % self.name)


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


class Room(object):
    def __init__(self, name, north, south, east, west, up, down, northeast, northwest, southeast, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.northeast = northeast
        self.northwest = northwest
        self.southeast = southeast
        self.description = description

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Instantiation of class Room
meridas_room = Room("Meridas Room", None, 'dining_room', 'parents_room', 'kitchen', None, None, None, None, None,
                    'Welcome to Meridas room! In here there is a bow and arrow, a sword, and a sack. \n'
                    'There is a door South, East, and West of the room.')
parents_room = Room("Parents Room", None, None, 'meridas_room', None, None, None, None, None, None,
                    'This is where the king and queen stay.\n'
                    'There is a dresser in the room and a door to the East.')
dining_room = Room("Dining Room", 'meridas_room', None, None, None, None, 'secret_room', None, None, None,
                   'There is a table in the middle of the room.\n'
                   'There is a shield on the wall and a bear statue in the corner.\n'
                   'There is a door to the north.')
kitchen = Room("Kitchen", 'outside', None, 'meridas_room', None, None, None, None, 'stables', None,
               'There is a door that leads Northwest, North, and East.\n'
               'In the kitchen, there is a cake on the table.\n'
               'There is a little crate on the floor next to the door.')
outside = Room("Outside", 'stables', 'kitchen', None, 'forest', None, None, None, None, 'fighting_area',
               'Out here is the main gate.\n'
               'West to the gate is the forest.\n'
               'You can also go South or Southeast.')
fighting_area = Room("Fighting Area", None, 'water', None, None, None, None, None, 'outside', None,
                     'Here are lots of '
                     'weapons.\n Off to the South there is water and some boats \n'
                     'Northwest leads to the gate to outside')
stables = Room("Stables", None, 'outside', None, None, None, None, 'kitchen', None, None,
               'Here are all the horses.\n'
               'There is hay and water here as well.\n'
               'You can go South or Northeast.')
forest = Room("Forest", None, 'fire_fall', 'outside', None, None, None, None, None, 'the_ring_of_stones',
              'There is a path to the South and to the Southeast.\n'
              'There is also a path that leads to the East')
fire_fall = Room("Fire Fall", 'forest', None, 'the_ring_of_stones', None, None, None, None, None, None,
                 'Here there is a water fall and a rock to climb.\n'
                 'Legends say that only kings were brave enough to drink from this water fall. \n'
                 'There are paths to North, and East')
the_ring_of_stones = Room("The Ring of Stones", None, None, 'witches_cottage', 'fire_fall', None, None, None, 'forest',
                          None, 'Here are stones that are placed in a circular pattern.\n'
                                'People said that The Ring of Stones tends to take you places to change your fate.\n'
                                'There are paths that lead to East, West, and Northwest')
witches_cottage = Room("Witches Cottage", None, None, None, 'the_ring_of_stones', 'dining_room', 'magic_room', None,
                       None, None, 'You have found the witches cottage.\n'
                                   'Inside you find many wood carvings, but one carving in the back catches your eye.\n'
                                   'You also find a strange looking rug on the floor in the back. \n'
                                   'From here you can go West.')
magic_room = Room("Magic Room", None, None, None, None, 'witches_cottage', None, None, None, None,
                  'This is where the witch does her magic.\n'
                  'The only way out is from the door you came in from.')
river = Room("River", 'the_ring_of_stones', None, None, None, None, None, 'ancient_kingdom_ruins', None, None,
             'There is a river that runs off into two separate rivers.\n'
             'Here you see some bears catching fish.\n'
             'There is a path that leads north')
ancient_kingdom_ruins = Room("Ancient Kingdom Ruins", None, None, None, None, None, 'moruds_cave', None, None, 'river',
                             'This is the old kingdom of Dunbroch before Mordu destroyed it.\n'
                             'You find the same symbol you saw in the castle of the three bears.\n'
                             'There is a path that leads down and another one that goes southeast.')
mordus_cave = Room("Mordus Cave", None, None, None, None, 'ancient_kingdom_ruins', None, None, None, None,
                   'Your in a dark cave with only faint light from above.\n'
                   'There are bones everywhere, and many broken weapons.\n'
                   'There is also a tapestry of four princes.\n'
                   'You hear heavy breathing behind you, and you see Mordu behind you.')
water = Room("Water", 'fighting_area', None, None, None, None, None, None, None, None,
             'Out here, there is a lake in front of you and some boats tied to the dock \n'
             'You can not go onto the boats.')

current_node = meridas_room
directions = ['north', 'south', 'east', 'west', 'up', 'down', 'northeast', 'northwest', 'southeast']
short_directions = ['n', 's', 'e', 'w', 'u', 'd', 'ne', 'nw', 'se']

while True:
    print(current_node.name)
    print(current_node.description)
    command = input('> ').strip().lower()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        # Finds the command in short directions (index number)
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go that way.")
    else:
        print("Command not Recognized")


# 1st import statements
# 2nd class definition
# - Items
# -Characters
# - Rooms
# 3rd instantiation of classes
# 4th controller