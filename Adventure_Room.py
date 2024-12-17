rooms = {"room1":{"E":"room2","S":"room4"},
         "room2":{"E":"room3","S":"room5","W":"room1"},
         "room3":{"W":"room2","S":"room6"},
         "room4":{"N": "room1","E":"room5"},
         "room5":{"W":"room4","N":"room2","E":"room6"},
         "room6":{"W":"room5","N":"room3"}}


def choose_direction(room):
    print("You are in a room. There are direction in following directions:")
    print(room[room])
    choice = input("which direction?")
    return room[choice]




