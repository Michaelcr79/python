"""
Date=raw_input("Please enter the date:")
print("The date you entered is " + Date)
print("We are going to find out whether or not you like candy.")
"""

"""
Candy=raw_input("Do you like candy?:").lower()

if Candy=='yes':
   print("You like candy")
elif Candy == 'no':
    print("You do not like candy")
else:
    print("Please enter Yes or No")
"""

"""
import time
for counter in range(10,0,-1):
    print(counter)
    time.sleep(5)
"""

"""
import time
shoppingCart=["jeans","pants","jacket","shoes","belt"]
for item in shoppingCart:
    print(item)
    time.sleep(.5)
"""
"""
import time

for counting in range(8,0,-2):
    print(counting)
    time.sleep(.5)
"""

"""
my_list=['one','two','three','four','five']
my_list_len=len(my_list)
for i in range(0,my_list_len):
    print(my_list[i])
"""
"""
import time
counter=1
while counter<11:
    print(counter)
    time.sleep(.5)
    counter=counter+1
    time.sleep(.5)
"""
"""
Best_bands_list=["The Beatles","Rolling Stones","Led Zeppelin","Jimmy Hendrix"]
print Best_bands_list[0] + "These are the best bands!"
Best_bands_list.append("The Temptations")
print Best_bands_list
Best_bands_list[2]="James Brown"
print Best_bands_list
"""

"""
import time
Best_bands_list=["The Beatles","Rolling Stones","Led Zeppelin","Jimmy Hendrix"]
for band in Best_bands_list:
    print(band + " are a great band!")
    print("Hello World")
    time.sleep(.5)
"""

"""
Birthday_Dictionary={'Emily':'June 1950','Sara':'November 1980'}
print Birthday_Dictionary['Emily']
"""

def Subtraction(A,B):
    subtract = A-B
    return subtract

print Subtraction(20,10) # This is calling the function.
