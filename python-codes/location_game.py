locations = {
0:{"desc":"You are sitting in front of tyhe computer learning python",
   "exits":{},
   "named_exits":{}},
1:{"desc":"You are standing on the road before the brick building",
   "exits":{"W":2, "E":3, "N":5, "S":4, "Q":0},
   "named_exits":{"2":2,"3":3,"5":5,"4":4}},
2:{"desc":"You are at the top of the hill",
  "exits":{"N":5, "Q":0},
  "named_exits":{"5":5}},
3:{"desc":"You are inside the building, a well house for a small stream",
   "exits":{"W":1, "Q":0},
   "named_exits":{"1":1}},
4:{"desc":"You are in a valley besides the stream",
   "exits":{"N":1, "W":2, "Q":0},
   "named_exits":{"1":1, "2":2}},
5:{"desc":"You are in the forest",
   "exits":{"W":2, "S":1, "Q":0},
   "named_exits":{"2":2,"1":1}}
}

vocab ={"QUIT":"Q",
        "EAST":"E",
        "WEST":"W",
        "NORTH":"N",
        "SOUTH":"S",
        "ROAD":"1",
        "HILL":"2",
        "BUILDING":"3",
        "VALLEY":"4",
        "FOREST":"5"
         }

# print(locations[0].split())
# print(locations[3].split(","))
# print(" ".join(locations[0].split()))

loc = 1

while True:
        available_Exits = ", ".join(locations[loc]["exits"].keys())
        print(locations[loc]["desc"])
        if loc == 0:
                break
        else:
            allExits = locations[loc]["exits"].copy()
            allExits.update(locations[loc]["named_exits"])    

        direction = input("Available exits are: "+ available_Exits+" ").upper()
        print()

        if len(direction) > 1:
                words = direction.split()
                for word in words:
                        if word in vocab:
                                direction = vocab[word]
                                break

        if direction in allExits:
            loc = allExits[direction]
        else:
                print("you can't go in that direction. ")               
    
