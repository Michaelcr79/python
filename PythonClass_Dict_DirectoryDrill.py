print 'Welcome!'
def start():
    people_dictionary = {'brett' : ['Male','Weight 175'],
        'nancy' : ['Female','Weight 125'],
        'patrick' : ['Male','Weight 195'],
        'diane' : ['Female','Weight 115'],
        'adam' : ['Male','Weight 215']}
    userName = raw_input('Please type in a name: ').lower()
    print 'You typed in the name ' + userName.title()
    try:
        Persons_Data = people_dictionary[userName]
        print 'Name: ' + userName.title() 
        print 'Sex: ' + Persons_Data[0]
        print 'Weight: ' + Persons_Data[1]
        print '\n'
        more()
    except:
        print 'That name (as written) was not found in the dictionary.'
        print '\n'
        more()

def more():
    More = raw_input('Search for another name? Enter Yes or No: ').lower()
    if  More == 'no':
        return
    if More == 'yes':
        start()
    else:
        print "Please enter Yes or No."
        more()

start()
