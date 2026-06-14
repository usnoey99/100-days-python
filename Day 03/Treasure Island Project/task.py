import emoji
#print("\n") 빈 줄 출력 (줄바꿈으로 해석)
#print(r"\n") \n 출력 (글자 그대로)
#print('''text''') 줄바꿈을 그대로 표현 가능
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
print(emoji.emojize("Welcome to Treasure Island🏝️.\nYour mission is to find the treasure."))

choose1 = input(emoji.emojize("You're at a cross road. Where do you want to go? left:left_arrow: or right:right_arrow:? "))
if choose1 == "left":
    choose2 = input(emoji.emojize("You've come to a lake. There is an island in the middle of the lake:national_park:."
                    "\nYou can wait for a boat or swim across. wait🧍 or swim🏊? "))
    if choose2 == "wait":
        choose3 = input(emoji.emojize("Suddenly, three coloured doors :door: appeared in front of you."
                        "\nWhich colour door would you like to open? red🟥, blue🟦left"
                                      " or yellow🟨? "))
        if choose3 == "red":
            print(emoji.emojize("You burned by fire.\n:skull: GAME OVER :skull:"))
        elif choose3 == "yellow":
            print(emoji.emojize("Wow! You finally found the Treasure! :gem_stone:\n:sparkles: You win :sparkles:"))
        elif choose3 == "blue":
            print(emoji.emojize("You are eaten by beasts.\n:skull: GAME OVER :skull:"))
        else:
            print(emoji.emojize("You are trapped on this island forever.\n:skull_and_crossbones: GAME OVER :skull_and_crossbones:"))
    else:
        print(emoji.emojize("You attacked by trout.\n:skull: GAME OVER :skull:"))

else:
    print(emoji.emojize("You fell into a hole.\n:skull: GAME OVER :skull:"))



