albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]
song_list_index = 3
song_title_index = 1 

#print("Choose your album to play:")        
while True:
    print("\t Please choose your album (invalid choice exists):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index+1,title))
    print()


    choice = int(input("enter your choice: "))
    if choice in range(len(albums)):
        song_list = albums[choice-1][song_list_index]
        #print(song_list)

    else:
        break    

    for number, song in song_list:
        print("{}: {}".format(number, song))

    print()    
    song_choice = int(input("Please choose the song to play: "))
    if song_choice in range(len(song_list)):
        print("Playing --->--->--- {}" .format(song_list[song_choice-1][song_title_index]))
        print()
       
