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
 _________|___________| ;`-.o`"=._; ." ` '`."  ` . "-._ /_______________|_______
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
print("You're at a crossroad. Will you turn left or right?")
turn_at_crossroad = input('Type "left" or "right"\n').lower()

if turn_at_crossroad != "left":
    print("You find the lair of huge frog. The frog eats you. Game over.")
    exit()

print("You carry on your journey and end up at a small lake in the center of the island.")
lake_decision = input('Type "wait" to stop and think for a way over the water or "swim" to try and swim across.\n').lower()

if lake_decision != "wait":
    print("You try to swim across the lake. Suddenly your leg is stuck! You realize a giant frog has caught your leg and"
          " is pulling you under. Game over.")
    exit()

print("You are thinking about your next move at the lake shore, when all of a sudden a huge rat swims next to you. "
      "You ask for a ride across"
      "and the gentle giant rat agrees and takes you over the water.")

print("There is a small castle in the middle of the lake. You go inside. There you find three doors.")
door_decision = input('Choose your fate! Will you open the "Red", "Yellow" or "Blue" door?\n').lower()

if  door_decision == "red":
    print("You open the red door and the room is suddenly filled with fire. Game over.")
    exit()
elif door_decision == "blue":
    print("You open the blue door. Inside there are frogs. They look hungry. "
          "You try to run but you slip in their mucus and fall over."
          "The frogs eat you alive. Game over.")
    exit()
elif door_decision == "yellow":
    print("You open the door. You are blinded by a shining light. It takes a moment for your eyes to adjust to the light. "
          "You see a golden frog figure in the middle of the room. Congratulations you win the game!")
    exit()
else:
    print("You are taking long to decide your choice. "
          "Suddenly the floor beneath you disappears and you fall fall fall down into the darkness. "
          "Game over.")

