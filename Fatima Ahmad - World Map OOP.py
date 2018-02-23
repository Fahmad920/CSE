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


# west_house = Room("West of House", 'north_house')
# north_house = Room("North of House", None)


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
kitchen = Room("Kitchen",)