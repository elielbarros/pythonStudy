"""
It is possible to iterate over list inside list.
It is possible to use any type on list including a Tuple and access items from this tuple
"""

rooms = [
    ['chair_1', 'chair_2'],
    ['chair_3', 'chair_4'],
    ['chair_5', 'chair_6']
]

for index, room in enumerate(rooms):
    for chair in room:
        print(index, chair)

rooms = [
    ['chair_1', 'chair_2'],
    ['chair_3', 'chair_4'],
    ['chair_5', 'chair_6', (0, 10, 20, 30)]
]

print(rooms[2][2][3])
