year = input("Which year do you want to check?: ")

if year % 4 == 0:
    if year % 100 == 00:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year.")
    else:
        print("Leap year")
else:
    print("Not leap year")

# Awnser:
# In the line 1 change the input from str to int.