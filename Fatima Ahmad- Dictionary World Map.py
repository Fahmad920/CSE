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

# at least 15 rooms
# Brave setting
# obstacles: witch , Mordu, Wilo-the-wisp]


brave_map = {
    'MERIDASROOM': {
        'NAME': 'MERIDAS ROOM',
        'DESCRIPTION': 'Welcome to Meridas room! In here there is a bow and arrow, a sword, and a sack. \n'
                       'There is a door North, South, East, and West of the room.',
        'PATHS': {
            'WEST': 'KITCHEN',
            'SOUTH': 'DINING ROOM',
            'EAST': 'PARENTS ROOM'
        }
    },
    'PARENTSROOM': {
        'NAME': 'PARENTS ROOM',
        'DESCRIPTION': 'This is where the king and queen stay.\n'
                       'There is a dresser in the room and a door to the West.',
        'PATHS': {
            'WEST': 'MERIDASROOM'
        }
    },
    'DININGROOM': {
        'NAME': 'DINING ROOM',
        'DESCRIPTION': 'There is a table in the middle of the room.\n'
                       'There is a shield on the wall and a bear statue in the corner.\n'
                       'There is a door to the north.',
        'PATHS': {
            'WEST': 'MERIDAS ROOM',
            'DOWN': 'SECRET ROOM'
        }
    },
    'KITCHEN': {
        'NAME': 'KITCHEN',
        'DESCRIPTION': 'There is a door that leads North and West.\n'
                       'In the kitchen, there is a cake on the table and a box.\n'
                       'There is a little crate on the floor next to the door.',
        'PATHS': {
            'WEST': 'STABLES',
            'NORTH': 'GATE'
        }
    },
    'OUTSIDE': {
        'NAME': 'OUTSIDE',
        'DESCRIPTION': 'Out here is the main gate.\n'
                       'West to the gate are the stables.\n'
                       'The gate out leads to the forest.',
        'PATHS': {
            'NORTH': 'FOREST',
            'WEST': 'STABLES',
            'SOUTH': 'KITCHEN'
        }
    },
    'FIGHTINGAREA': {
        'NAME': 'FIGHTING AREA',
        'DESCRIPTION': 'Here are lots of weapons.\n'
                       'Off to the North there is water and some boats',
        'PATHS': {
            'NORTH': 'OUTSIDE',
            'SOUTH': 'WATER'
        }
    },
    'STABLES': {
        'NAME': 'STABLES',
        'DESCRIPTION': 'Here are all the horses.\n'
                       'There is hay and water here as well.',
        'PATHS': {
            'SOUTH': 'STABLES',
            'WEST': 'OUTSIDE'
        }
    },
    'FOREST': {
        'NAME': 'FOREST',
        'DESCRIPTION': 'There is a path to the south.\n'
                       'There is a path that leads to the North and to the East',
        'PATHS': {
            'SOUTH': 'FIREFALL',
            'EAST': 'MAZE',
            'NORTH': 'OUTSIDE'
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
            'NORTH': 'FOREST',
            'WEST': 'FIRE FALL'
        }
    },
    'WITCHES COTTAGE': {
        'NAME': 'WITCHES COTTAGE',
        'DESCRIPTION': 'You have found the witches.\n'
                       'Inside you find many wood carvings, but a special carving in the back catches your eye.',
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
            'EAST': 'ANCIENT KINGDOM RUINS'
        }
    },
    'ANCIENT KINGDOM RUINS': {
        'NAME': 'ANCIENT KINGDOM RUINS',
        'DESCRIPTION': 'This is the old kingdom of Dunbroch before Mordu destroyed it.\n'
                       'You find the same symbol you seen in the castle of the three bears in a circular pattern.\n'
                       'There is only one path that leads down.',
        'PATHS': {
            'DOWN': 'MORDUS CAVE'
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

current_node = brave_map['MERIDASROOM']
direCtions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in direCtions:
        print("You moVed")
    else:
        print("Command not ReCognized")  

