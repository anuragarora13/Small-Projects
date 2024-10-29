print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
  ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction=input('you  a\'re at the crossroad, Where do you want to go "left" or "right"')
if direction.capitalize()=='Left':
    direction=input(' you came to a lake and there is an island in the middle of the lake.'
                    ' type "swim" or "wait" for the boat?')
    if direction.capitalize()=='Wait':
        door=input('Do you want to go by which door(Red/Blue/yellow/Anything else')
        if door.capitalize()=='Yellow':
            print('You win')
        elif door.capitalize()=='Red':
            print('Burned by Fire')
            print('Game over.')
        elif door.capitalize()=='Blue':
            print('Eaten By beast')
            print("Game over.")
        else:
            print('Game over')
    else:
        print('Attacked by trout')
        print('Game Over')
else:
    print('fall into a hole ')
    print('Game over')



