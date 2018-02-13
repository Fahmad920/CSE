#world_map = {
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
# obstables: witch , Mordu, Wilo-the-wisp


brave_map = {
     'MERIDAS ROOM':{
         'NAME': 'MERIDAS ROOM',
         'DESCRIPTION': 'Welcome to Meridas room! In here there is a bow and arrow, a sword, and a sack.',
         'There is a door North, South, East, and West of the room.'
         'PATHS': {
             'WEST': 'KITCHEN',
             'SOUTH': 'DINING ROOM',
             'EAST': 'PARENTS ROOM'
         }
    },
    'PARENTSROOM':{
        'NAME': 'PARENTSROOM',
        'DESCRIPTION':'This is where the king and queen stay.',
                      'There is a dresser in the room and a door to the East.'
        'PATHS': {
            'EAST': 'MERIDASROOM'
        }
    },
    'DININGROOM':{
        'NAME': 'DININGROOM',
        'DESCRIPTION': 'There is a table in the middle of the room.',
        'There is a shield on the wall and a bear statue in the corner.'
        'There is a door to the north.'
        'PATHS': {
            'NORTH': 'MERIDASROOM',
            'DOWN': 'SECRET ROOM'
        }
    },
    'KITCHEN': {
        'NAME': 'KITCHEN',
        'DESCRIPTION': 'There is a door going north.',
        'In the kitchen, there is a cake on the table and a box.'
        'There is a little crate on the floor next to the door.'
        'PATHS':{
            'WEST': 'STABLES',
            'NORTH': 'GATE'
        }
    },
    'OUTSIDE': {
        'NAME': 'OUTSIDE',
        'DESCRIPTION': 'Out here is the main gate.',
        'West to the gate are the stables.'
        'The gate out leads to the forest.'
        'PATHS': {
            'NORTH': 'FOREST',
            'WEST': 'STABLES',
            'SOUTH': 'KITCHEN'
         }
    },
    'FIGHTINGAREA': {
        'NAME': 'FIGHTINGAREA',
        'DESCRIPTION': 'Here are lots of weapons.',
        'Off to the North there is water and some boats'
        'PATHS':{
            'NORTH': 'OUTSIDE',
            'SOUTH': 'WATER'
        }
    },
    'STABLES': {
        'NAME': 'STABLES',
        'DESCRIPTION':'Here are all the horses.',
        'There is hay and water here as well'
        'PATHS': {
            'SOUTH': 'STABLES',
            'WEST': 'OUTSIDE'
     }
    },
    'FOREST': {
        'NAME': 'FOREST',
        'DESCRIPTION': 'There is a path to the south.',
        'There is a path that leads to the North and to the East'
        'PATHS': {
            'SOUTH': 'FIREFALL',
            'EAST': 'MAZE',
            'NORTH': 'OUTSIDE'
        }
    },
    'FIREFALL':{
        'NAME': 'FIREFALL',
        'DESCRIPTION': 'Here there is a water fall and a rock to climb.',
        'Legends say that only kings were brave enough to drink from this water fall.'
        'PATHS':{
            'NORTH': 'FOREST',
            'EAST': 'THE RING OF STONES'
        }
    },
    'THE RING OF STONES':{
        'NAME': 'THE RING OF STONES',
        'DESCRIPTION': 'Here are stones that are placed in a circular pattern.',
        'People have said that The Ring of Stones tends to take you places to change your fate.'
        'PATHS':{
            'EAST': 'WITCHES COTTAGE',
            'NORTH': 'FOREST',
            'WEST': 'FIRE FALL'
        }
    },
    'WITCHES COTTAGE':{
        'NAME': 'WITCHES COTTAGE',
        'DESCRIPTION': 'You have found the witches ',
        'Inside you find many wood carvings, but a special carving in the back catches your eye.'
        'PATHS':{
            'WEST': 'THE RING OF STONES',
            'DOWN': 'MAGIC ROOM',
            'UP': 'DINING ROOM'
        }
    },
    'MAGIC ROOM':{
        'NAME': 'SECRET MAGIC ROOM',
        'DESCRIPTION': 'This is where the witch does her magic.',
        'The only way out is from the door you came in from.'
        'PATHS': {
            'UP': 'WITCHES COTTAGE'
        }
    },
    'RIVER':{
        'NAME': 'RIVER',
        'DESCRIPTION': 'There is a river that runs off into two separate rivers.',
        'Here you see some bears catching fish.'
        'There is a path that leads north'
        'PATH': {
            'NORTH': 'THE RING OF STONE',
            'EAST': 'ANCIENT KINGDOM RUINS'
        }
    },
    'ANCIENT KINGDOM RUINS':{
        'NAME': 'ANCIENT KINGDOM RUINS',
        'DESCRIPTION': 'This is the old kingdom of Dunbroch before Mordu destroyed it.',
        'Here you find the same symbol you seen in the castle of the three bears in a circular pattern.'
        'There is only one path that leads down.'
    'PATHS':{
        'DOWN': 'MORDUS CAVE'
    }

    },
    ''

}
