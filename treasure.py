print(r'''
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
print("Welcome to Treasure Island.\n Your mission is to find the treasure.")

direction = input("Where would you like to go first? Left or Right?" )

if direction == "Left":
    print("You have successfully found an ocean that puts you closer to the treasure!")
    swim = input("Would you swim or wait a rescue boat? Type 'swim' or wait'" )
    if swim == "swim":
        print("You have drowned! Try again.")
    elif swim == "wait":
        print("The rescue boat is coming! Now you have reached the treasure island!")
        door = input("Now you have to choose which door to go through! There's red, blue, and yellow door. Type R for red, B for blue, and Y for yellow. ")
        if "R" == door == "B":
            print("You have picked the wrong door! Game Over. Try again next time.")
        elif door == "Y":
            print("You have located the treasure! Congratulations!")
        else:
            print("You may have typed the wrong input. Try again.")

    else:
        print("You may have typed the wrong input. Try again.")

elif direction == "Right":
    print("You have a found a dragon!! You have been killed. Try again.")
else:
    print("You may have typed the wrong input. Try again.")


