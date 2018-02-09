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
         'DESCRIPTION': 'Welome to Meridas room! In here there is a bow and arrow, a sword, and a sack.',
         'There is a door North, South, East, and West of the room.'
         'PATHS': {
             'WEST': 'KITCHEN',
             'SOUTH': 'DINING ROOM',
             'EAST': 'PARENTS ROOM'
         }
    },
}