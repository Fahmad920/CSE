# world_map = {
#     'WESTHOUSE':{
#         'NAME': 'WEST OF HOUSE',
#         'DESCRIPTION': 'You are west of a small house',
#         'PATHS': {
#             'NORTH': 'NORTHHOUSE',
#             'SOUTH': 'SOUTHHOUSE'
#         }
#     },
#     'NORTHHOUSE': {
#         'NAME': 'NORTH OF HOUSE',
#         'DESCRIPTION': 'Insert description here',
#         'PATHS': {
#             'WEST': 'WESTHOUSE'
#         }
#     },
#     'SOUTHHOUSE': {
#         'NAME': 'SOUTH OF HOUSE',
#         'DESCRIPTION': 'Insert description here',
#         'PATHS': {
#             'WEST': 'WESTHOUSE'
#         }
#     }
# }
#
# current_node = world_map['SOUTHHOUSE']
# print(current_node['DESCRIPTION'])


brave_map = {
    'MERIDAS ROOM': {
        'NAME': 'MERIDAS ROOM',
        'DESCRIPTION': 'Welcome to Meridas room! In here there is a bow and arrow, a sword, and a sack. \n'
                       'There is a door South, East, and West of the room.',
        'PATHS': {
            'WEST': 'KITCHEN',
            'SOUTH': 'DINING ROOM',
            'EAST': 'PARENTS ROOM'
        }
    },
    'PARENTS ROOM': {
        'NAME': 'PARENTS ROOM',
        'DESCRIPTION': 'This is where the king and queen stay.\n'
                       'There is a dresser in the room and a door to the East.',
        'PATHS': {
            'EAST': 'MERIDAS ROOM'
        }
    },
    'DINING ROOM': {
        'NAME': 'DINING ROOM',
        'DESCRIPTION': 'There is a table in the middle of the room.\n'
                       'There is a shield on the wall and a bear statue in the corner.\n'
                       'There is a door to the north.',
        'PATHS': {
            'NORTH': 'MERIDAS ROOM',
            'DOWN': 'SECRET ROOM'
        }
    },
    'KITCHEN': {
        'NAME': 'KITCHEN',
        'DESCRIPTION': 'There is a door that leads Northwest, North, and East.\n'
                       'In the kitchen, there is a cake on the table and a box.\n'
                       'There is a little crate on the floor next to the door.',
        'PATHS': {
            'NORTHWEST': 'STABLES',
            'NORTH': 'GATE',
            'EAST': 'MERIDAS ROOM'
        }
    },
    'OUTSIDE': {
        'NAME': 'OUTSIDE',
        'DESCRIPTION': 'Out here is the main gate.\n'
                       'West to the gate is the forest.\n'
                       'You can also go South or Southeast.',
        'PATHS': {
            'WEST': 'FOREST',
            'NORTH': 'STABLES',
            'SOUTH': 'KITCHEN',
            'SOUTHEAST': 'FIGHTING AREA'
        }
    },
    'FIGHTINGAREA': {
        'NAME': 'FIGHTING AREA',
        'DESCRIPTION': 'Here are lots of weapons.\n'
                       'Off to the South there is water and some boats',
        'Northwest leads to the gate to outside'
        'PATHS': {
            'NORTHWEST': 'OUTSIDE',
            'SOUTH': 'WATER'
        }
    },
    'STABLES': {
        'NAME': 'STABLES',
        'DESCRIPTION': 'Here are all the horses.\n'
                       'There is hay and water here as well.\n'
                       'You can go South or Northeast.',
        'PATHS': {
            'SOUTH': 'OUTSIDE',
            'NORTHEAST': 'KITCHEN',
        }
    },
    'FOREST': {
        'NAME': 'FOREST',
        'DESCRIPTION': 'There is a path to the South and to the Southeast.\n'
                       'There is also a path that leads to the East',
        'PATHS': {
            'SOUTH': 'FIREFALL',
            'EAST': 'OUTSIDE',
            'SOUTHEAST': 'THE RING OF STONES'
        }
    },
    'FIREFALL': {
        'NAME': 'FIREFALL',
        'DESCRIPTION': 'Here there is a water fall and a rock to climb.\n'
                       'Legends say that only kings were brave enough to drink from this water fall.',
        'PATHS': {
            'NORTH': 'FOREST',
            'EAST': 'THE RING OF STONES'
        }
    },
    'THE RING OF STONES': {
        'NAME': 'THE RING OF STONES',
        'DESCRIPTION': 'Here are stones that are placed in a circular pattern.\n'
                       'People have said that The Ring of Stones tends to take you places to change your fate.',
        'PATHS': {
            'EAST': 'WITCHES COTTAGE',
            'NORTHWEST': 'FOREST',
            'WEST': 'FIRE FALL'
        }
    },
    'WITCHES COTTAGE': {
        'NAME': 'WITCHES COTTAGE',
        'DESCRIPTION': 'You have found the witches cottage.\n'
                       'Inside you find many wood carvings, but a special carving in the back catches your eye.'
                       'You also find a strange looking rug on the floor in the back.',
        'PATHS': {
            'WEST': 'THE RING OF STONES',
            'DOWN': 'MAGIC ROOM',
            'UP': 'DINING ROOM'
        }
    },
    'MAGIC ROOM': {
        'NAME': 'SECRET MAGIC ROOM',
        'DESCRIPTION': 'This is where the witch does her magic.\n'
                       'The only way out is from the door you came in from.',
        'PATHS': {
            'UP': 'WITCHES COTTAGE'
        }
    },
    'RIVER': {
        'NAME': 'RIVER',
        'DESCRIPTION': 'There is a river that runs off into two separate rivers.\n'
                       'Here you see some bears catching fish.\n'
                       'There is a path that leads north',
        'PATH': {
            'NORTH': 'THE RING OF STONE',
            'NORTHEAST': 'ANCIENT KINGDOM RUINS'
        }
    },
    'ANCIENT KINGDOM RUINS': {
        'NAME': 'ANCIENT KINGDOM RUINS',
        'DESCRIPTION': 'This is the old kingdom of Dunbroch before Mordu destroyed it.\n'
                       'You find the same symbol you seen in the castle of the three bears in a circular pattern.\n'
                       'There is only one path that leads down.',
        'PATHS': {
            'DOWN': 'MORDUS CAVE',
            'SOUTHWEST': 'ANCIENT KINGDOM RUINS'
        }
    },
    'MORDUS CAVE': {
        'NAME': 'MORDUS CAVE',
        'DESCRIPTION': 'Your in a dark cave with only faint light from above.\n'
                       'There are bones everywhere, and many broken weapons.\n'
                       'There is also a tapestry of four princes.\n'
                       'You hear heavy breathing behind you, and you see Mordu behind you.',
        'PATHS': {
            'UP': 'MORDUS CAVE'
        }
    }
}

current_node = brave_map['MERIDAS ROOM']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN', 'NORTHEAST', 'NORTHWEST', 'SOUTHEAST', 'JUMP']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('> ').strip().upper()
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = brave_map[name_of_node]
        except KeyError:
            print("You cannot go that way.")
    else:
        print("Command not Recognized")
    if command == 'JUMP':
        print("WHOAHHHHHH")
    print()