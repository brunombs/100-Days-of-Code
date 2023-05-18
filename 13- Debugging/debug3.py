for number in range(1, 101):
    if number % 3 == 0 or number % 5 == 0:
        print("FizzBuzz")
    if number % 3 == 0:
        print("Fizz")
    if number % 5 == 0:
        print("Buzz")
    else:
        print([number])

# Awnser:
# Line 9: remove the [] in number.
# Line 1: change "or" for "and"
# Line 4: change "if" for "elif"
# Line 6: change "if" for "elif"