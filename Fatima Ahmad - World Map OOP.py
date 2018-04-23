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


class Character(object):
    def __init__(self, name, description, item, health):
        self.name = name
        self.description = description
        self.inventory = []
        self.item = item
        self.health = health

    def look(self):
        print("You have looked around")

    def climb(self):
        print("You have looked around")

    def take(self, item):
        self.inventory.append(item)
        print("You have taken something")

    def health(self):
        print("You have health")


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
kitchen = Room("Kitchen", 'gate', None, 'meridas_room', None, None, None, None, 'stables', None,
               'There is a door that leads Northwest, North, and East.\n'
               'In the kitchen, there is a cake on the table.\n'
               'There is a little crate on the floor next to the door.')
outside = Room("Outside", 'stables', 'kitchen', None, 'forest', None, None, None, None, 'fighting_area',
               'Out here is the main gate.\n'
               'West to the gate is the forest.\n'
               'You can also go South or Southeast.')
fighting_area = Room("Fighting Area", None, 'water', None, None, None, None, None, 'outside', None,
                     'Here are lots of '
                     'weapons.\n Off to the South there is water and some boats'
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
                 'Legends say that only kings were brave enough to drink from this water fall.')
the_ring_of_stones = Room("The Ring of Stones", None, None, 'witches_cottage', 'fire_fall', None, None, None, 'forest',
                          None, 'Here are stones that are placed in a circular pattern.\n'
                                'People said that The Ring of Stones tends to take you places to change your fate.')
witches_cottage = Room("Witches Cottage", None, None, None, 'the_ring_of_stones', 'dining_room', 'magic_room', None,
                       None, None, 'You have found the witches cottage.\n'
                                   'Inside you find many wood carvings, but one carving in the back catches your eye.'
                                   'You also find a strange looking rug on the floor in the back.')
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
                             'There is only one path that leads down.')
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

# Key error = when you look in a dictionary for a variable, but there is no item in there
# errethmetic error = when you try to divide by 0
