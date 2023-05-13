print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
''')
print('Welcome to Treasure Island')
print('Your mission is to find the treasure.')

while True:
    firststep = input('Left or right? ').lower()
    if firststep == "right" or firststep == "left":
        break
    else:
        print("Invalid input. Please enter 'left' or 'right'.")

if firststep == "right":
    print("Fall into a hole.")
    print('Game over.')
elif firststep == "left":
    print('Good move. You are in level 2 now.')

    while True:
        secondstep = input("Swim or wait? ").lower()
        if secondstep == "swim" or secondstep == "wait":
            break
        else:
            print("Invalid input. Please enter 'swim' or 'wait'.")

    if secondstep == "swim":
        print("Attacked by a trout.")
        print("Game over.")
    elif secondstep == "wait":
        print('Very good. Now you are in level 3.')

        while True:
            thirdstep = input("Red, blue or yellow? ").lower()
            if thirdstep == "red" or thirdstep == "blue" or thirdstep == "yellow":
                break
            else:
                print("Invalid input. Please enter 'red', 'blue', or 'yellow'.")

        if thirdstep == "yellow":
            print("You win.")
        elif thirdstep == "red":
            print("Burned by fire.")
            print("Game over.")
        elif thirdstep == "blue":
            print("Eaten by beasts.")
            print("Game over.")
