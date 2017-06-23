#!/usr/bin/python
# A simple text based game in Python.



def move_east():
    global inner_location
    inner_location = inner_location + 1



def move_west():
    global inner_location
    inner_location = inner_location - 1


    
def reset_location():
    global current_location
    global inner_location
    global movesInDesert
    if command=='move east':
        move_east()
        if inner_location > 2:
            current_location = current_location + 1
            inner_location = 0
            if current_location == 3:
                current_location = 2
                inner_location = 2
                print ("Reached eastern border!")
            if current_location == 6:
                current_location = 5
                inner_location = 2
                print ("Reached eastern border!")
            if current_location == 9:
                current_location = 8
                inner_location = 2
                print ("Reached eastern border!")
        else:
            movesInDesert = movesInDesert + 1

        if current_location > 11:
            current_location = 11 
            inner_location == 2
            print "Reached eastern border!"
        else:
            movesInDesert = movesInDesert + 1

    if command=='move west':
        move_west()
        if inner_location < 0:
            current_location = current_location - 1
            inner_location = 2
            if current_location == 2:
                current_location = 3
                inner_location = 0
                print ("Reached western border!")
            if current_location == 5:
                current_location = 6
                inner_location = 0
                print ("Reached western border!")
            if current_location == 8:
                current_location = 9
                inner_location = 0
                print ("Reached western border!")
        else:
            movesInDesert = movesInDesert + 1

        if current_location < 0:
            current_location = 0
            inner_location = 0
            print "Reached western border!"
        else:
            movesInDesert = movesInDesert + 1

    if command=='move north':
        if current_location > 2 and current_location <=11:
            current_location = current_location - 3
            movesInDesert = movesInDesert + 1
        else:
            print "Cannot move any further north!"

    if command=='move south':
        if current_location > -1 and current_location <= 8:
            current_location = current_location + 3
            movesInDesert = movesInDesert + 1
        else:
            print "Cannot move any further south!"



def dig_with_shovel():
   global current_location
   global inventory
   global inner_location
   if inventory['shovel']==1:
        print("You dig for a while.")
        if current_location==6 and inner_location==1 and locations[6]==('d,c,d'):            
            print("Found and retrieved an empty canteen off the sand!")
            inventory['canteen']=1
            locations[6] = ('d,d,d')
        else:
            print("You found nothing but sand!")
   else:
       print("You are a civilized explorer, you need a shovel!")



def get_shovel():
    global current_location
    global inventory
    global inner_location 
    if inventory['shovel']==1:
        print("You already have the shovel!")
    elif locations[8] == ('d,h,d') and inner_location==1:
        print("You retrieve the shovel off the desert sands!")
        locations[8] = ('d,d,d')
        inventory['shovel']=1 
    else:
        print("You don't see a shovel here.")



def fill_canteen():
    global current_location
    global inventory
    global inner_location
    if inventory['canteen']==0:
        print "You need a canteen to fill one!"
        return

    if locations[current_location]==('d,o,d') and inner_location==1:
        print("You fill the canteen with life giving water!")
        inventory['canteen']=11
    else:
        print("There is no water here to fill the canteen with.")



def drink():
    global inventory
    global movesInDesert
    if inventory['canteen'] > 1:
        inventory['canteen'] = inventory['canteen'] - 1
        print("My that's refreshing!!!");
        movesInDesert=0
    else:
        print("Don't have a canteen or canteen is empty!")



def look():
        global current_location
        global locations
        global inner_location

        if locations[current_location] == ('d,d,d'):
            print ("You see nothing but desert.")
        elif locations[current_location] == ('d,o,d'):
            if inner_location == 1: 
                print("You are at an oasis!")
            else:
                print("You are near an oasis!")
        elif locations[current_location] == ('d,s,d'):
            if inner_location == 1:
                print("You are where you started your adventure!")
            else:
                print("You are close to where you began the adventure!")
        elif locations[current_location] == ('d,h,d'):
            if inner_location == 1:
                print ("You see a shovel on the sand!")
            else:
                print ("You are in the desert")
        elif locations[current_location] == ('d,t,d'):
            if inner_location == 1:
                print ("You are at the base of a fig tree.")
            else:
                print ("You are near a tree.")
        else:
            print("You are in the desert.")

        return



def inventory_check():
    global inventory
    print ("You are carrying:")
    if inventory['canteen'] > 0:
        print "A canteen with " + str(inventory['canteen']) + " drinks left."
    if inventory['shovel'] > 0:
        print "A shovel."
    return



def status_thirst(movesInDesert):
    if movesInDesert >= 6 and movesInDesert <= 12:
        print ("You are thirsty.")
    if movesInDesert >= 12 and movesInDesert <= 18:
        print ("You are very thirsty.")
    if movesInDesert >= 18 and movesInDesert <= 24:
        print ("You are dying of thirst!")
    if movesInDesert > 24:
        print ("You have died of thirst!")
        quit()
    return


def play_game():
    global command_list
    command_list=['move north','move south','move west','move east',
                  'drink', 'get shovel', 'dig with shovel', 'fill canteen']

    # o means oasis.  c means canteen.  h means shovel.  s means start.
    # d means desert.   t means fig tree.
    global locations
    locations = [ ('d,t,d'),('d,d,d'),('d,d,d'),
                  ('d,d,d'),('d,s,d'),('d,d,d'),
                  ('d,c,d'),('d,o,d'),('d,h,d'), 
                  ('d,d,d'),('d,d,d'),('d,d,d')
                ]

    global current_location
    global inner_location
    global inventory
    global movesInDesert
    current_location=4 # Begin at d,s,d always.
    inner_location=1
    inventory={'shovel':0,'canteen':0}
    movesInDesert = 0; # Maximum allowed moves in desert is ???.

    won = 0        
    while(won==0):
        status_thirst(movesInDesert)

        look()

        global command
        command=raw_input("Command:")

        command = command.lower()

        if command == 'move west' or command == 'move east':
            reset_location()

        elif command == 'move north' or command == 'move south':
            reset_location()

        elif command == 'get shovel':
            get_shovel()

        elif command == 'dig with shovel':
            dig_with_shovel()

        elif command == 'fill canteen':
            fill_canteen()

        elif command == 'drink':
            drink()

        elif command == 'look':
            look()

        elif command == 'quit':
            quit()

        elif command == 'inventory':
            inventory_check()

        else:
            print ("I don't understand: ")
            print command + " \n"



play_game()
