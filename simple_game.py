# A simple text based game in Python.

def move_east(global inner_location):
    if inner_location == 0:
        inner_location = 1
    if inner_location == 1:
        inner_location = 2
    if inner_location == 2:
        inner_location = 0

def move_west(global inner_location):
    if inner_location == 0:
        inner_location = 2
    if inner_location == 1:
        inner_location = 0
    if inner_location == 2:
        inner_location = 1

    
def reset_location(global current_location,global inner_location):
    if command=='move east':
        move_east(inner_location)
        if inner_location == 0:
            current_location = current_location + 1
        if current_location > 8:
            current_location = 8
            inner_location == 2
        
    if command=='move west':
        move_west(inner_location)
        if inner_location == 2:
            current_location = current_location - 1
        if current_location < 0:
            current_location = 0
            inner_location = 0

    if command=='move north':
        if current_location > 2 and current_location <=8:
            current_location = current_location - 3

    if command=='move south':
        if current_location > -1 and current_location <= 5:
            current_location = current_location + 3

    print locations[current_location]
    print "current_location:"+str(current_location)
    print "inner_location:"+str(inner_location)

def dig_with_shovel(global current_location, global inventory, global inner_location):
    if inventory['shovel']==1:
        print("You dig for a while.")
    else:
        print("A civilized explorer will not dig without a shovel!")

    if current_location == 6 and inner_location == 1 and inventory['canteen']==0:
        print("Found an empty canteen!")
        inventory['canteen']==1

def get_shovel(global current_location, global inventory, global inner_location):
    if inventory['shovel']==1:
        print("You already have the shovel!")
    if current_location == 8 and inner_location == 1:
        print("You retrieve the shovel off the desert sands!")
    else:
        print("You don't see that here!")



def play_game():
    global command_list
    command_list=['move north','move south','move west','move east',
                  'drink', 'get shovel', 'get canteen',
                  'dig with shovel', 'fill canteen']

    # o means oasis.  c means canteen.  h means shovel.  s means start.
    # d means desert.
    global locations
    locations = [ ('d,d,d'),('d,o,d'),('d,d,d'),
                  ('d,d,d'),('d,s,d'),('d,d,d'),
                  ('d,c,d'),('d,d,d'),('d,h,d') ]

    global current_location
    global inner_location
    global inventory
    global movesInDesert
    current_location=4 # Begin at d,s,d always.
    inner_location=1
    inventory={'shovel':0,'canteen':0}
    movesInDesert = 0; # Maximum allowed moves in desert is 10.

    won = 0        
    while(won==0):
        global command
        command=raw_input("Command:")

        command = command.lower()

        if command == 'move west' or command == 'move east':
            reset_location(current_location,inner_location)

        if command == 'move north' or command == 'move south':
            reset_location(current_location,inner_location)

        if command == 'get shovel':
            get_shovel(current_location,inventory,inner_location)

        if command == 'dig with shovel':
            dig_with_shovel(current_location,inventory,inner_location)

play_game()
